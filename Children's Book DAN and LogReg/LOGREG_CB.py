import numpy as np
from datasets import load_dataset
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score
from sklearn.preprocessing import StandardScaler

from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased", return_tensors='pt', truncation_side='left')

def preprocess_function(examples) :
    contexts = [["".join(sentence)]*10 for sentence in examples["sentences"]] # list of sentences
    questions = [question for question in examples['question']]

    options = [option for option in examples['options']] # list of list
    questions = [[questions[idx].replace("XXXXX", option) for option in options] for idx, options in enumerate(options)]

    answers = examples['answer']
    labels = [options[idx].index(answer) for idx, answer in enumerate(answers)]

    contexts = sum(contexts, [])
    questions = sum(questions, [])

    tokenized_examples = tokenizer(contexts, questions, truncation="only_first", max_length=256)
    tokenized_examples = {k: [v[i : i + 10] for i in range(0, len(v), 10)] for k, v in tokenized_examples.items()}

    def make_onehot(label) :
        answer = [0]*10
        answer[label] = 1
        return answer

    tokenized_examples['label'] = [make_onehot(label) for label in labels]
    return tokenized_examples

def flatten_input(data):
    X = []
    Y = []

    max_len = max(sum(len(item) for item in example['input_ids']) for example in data)

    for example in data:
        input_ids = example['input_ids']
        attention_mask = example['attention_mask']

        flat_input_ids = [item for sublist in input_ids for item in sublist]
        flat_attention_mask = [item for sublist in attention_mask for item in sublist]

        pad_length_input_ids = max_len - len(flat_input_ids)
        pad_length_attention_mask = max_len - len(flat_attention_mask)

        if pad_length_input_ids > 0:
            padded_input_ids = np.pad(flat_input_ids, (0, pad_length_input_ids), 'constant')
        else:
            padded_input_ids = flat_input_ids

        if pad_length_attention_mask > 0:
            padded_attention_mask = np.pad(flat_attention_mask, (0, pad_length_attention_mask), 'constant')
        else:
            padded_attention_mask = flat_attention_mask

        features = np.concatenate([padded_input_ids, padded_attention_mask])

        label = np.argmax(example['label'])

        X.append(features)
        Y.append(label)
    
    return np.array(X), np.array(Y)

if __name__ == '__main__':

    dataset = load_dataset('cbt', 'CN', split='train[:10000]')
    train_dataset, test_dataset = dataset.train_test_split(test_size=0.2).values()

    tokenized_train = train_dataset.map(preprocess_function, batched=True, num_proc=4, remove_columns=train_dataset.column_names)
    tokenized_test = test_dataset.map(preprocess_function, batched=True, num_proc=4, remove_columns=test_dataset.column_names)

    X_train, Y_train = flatten_input(tokenized_train)
    X_test, Y_test = flatten_input(tokenized_test)

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    model = LogisticRegression(max_iter=2000)
    model.fit(X_train_scaled, Y_train)

    y_pred = model.predict(X_test_scaled)

    accuracy = accuracy_score(Y_test, y_pred)
    f1 = f1_score(Y_test, y_pred, average='weighted')

    print("Accuracy:", accuracy)
    print("F1 Score:", f1)