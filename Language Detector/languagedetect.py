# language detection
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import streamlit as st

def main():

    # lang data from this github
    data = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/dataset.csv")
    print(data.head())

    # training and test
    x = np.array(data["Text"])
    y = np.array(data["language"])

    cv = CountVectorizer()
    X = cv.fit_transform(x)
    X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                        test_size=0.33, 
                                                        random_state=42)

    # multinomial naive bayes algorithm
    model = MultinomialNB()
    model.fit(X_train,y_train)
    model.score(X_test,y_test)

    st.title("Language Detection")
    user = st.text_area('Enter text here:')
    if user:
        data = cv.transform([user]).toarray()
        output = model.predict(data)
        st.title(str(output))
    

if __name__ == '__main__':
    main()