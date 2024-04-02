import docx2txt
import re
import nltk
import string
from pdfminer.high_level import extract_text

class Resume:
    PHONE_REGEX = re.compile(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]')

    SKILLS = [
        'machine learning',
        'python',
        'c',
        'c++',
        'russian'
    ]

    EDUCATION = [
        'school',
        'college',
        'university',
        'academy',
        'faculty',
        'institute',
        'faculdades',
        'Schola',
        'schule',
        'lise',
        'lyceum',
        'lycee',
        'polytechnic',
        'kolej',
        'üniversite',
        'okul',
    ]

    def __init__(self, body_text):
        self.body = body_text

    # HAS ISSUES
    def extract_education(self):
        sentences = nltk.sent_tokenize(self.body)
        education = []

        for sentence in sentences:
            for word in self.EDUCATION:
                if word.lower() in sentence.lower():
                    education.append(sentence)
                    break

        refined_education = []
        for edu in education:
            if ':' in edu:
                edu = edu.split(':')[1]
            edu = edu.strip().title()
            refined_education.append(edu)

        return list(set(refined_education))

    def extract_skills(self):
        stop_words = set(nltk.corpus.stopwords.words('english'))
        tokens = nltk.tokenize.word_tokenize(self.body)

        filtered_tokens = [w for w in tokens if w not in stop_words and w.isalpha()]

        bi_tri_grams = list(map(' '.join, nltk.everygrams(filtered_tokens, 2, 3)))

        found_skills = []
        for token in filtered_tokens:
            if token.lower() in self.SKILLS:
                found_skills.append(token)
        
        for ngram in bi_tri_grams:
            if ngram.lower() in self.SKILLS:
                found_skills.append(ngram)
        
        return found_skills

    def extract_phone_number(self):
        phone = re.findall(self.PHONE_REGEX, self.body)
        if phone:
            number = ''.join(phone[0])
            if self.body.find(number) >= 0 and len(number) < 16:
                return number
        return None

    def preprocess_text(self):
        chars_to_remove = string.punctuation + '\t' + '\n' + '•·●○'
        translator = str.maketrans('', '', chars_to_remove)
        self.body = self.body.translate(translator)
        return self.body

def extract_from_docx(path):
    text = docx2txt.process(path)
    return text.replace('\t', ' ') if text else None

def extract_from_pdf(path):
    return extract_text(path)

if __name__ == '__main__':
    resume_text = extract_from_pdf('./resume.pdf')
    resume = Resume(resume_text)

    resume.preprocess_text()

    skills = resume.extract_skills()
    phone_number = resume.extract_phone_number()
    education = resume.extract_education()

    print(skills, phone_number)
