import numpy as np
import nltk
# nltk.download('punkt')
from nltk.corpus import stopwords
# nltk.download('stopwords')
from nltk.stem import PorterStemmer


def transform_text(texts):
    transformed_texts = []
    for text in texts:
        text = text.lower()  # lower casing
        text = nltk.word_tokenize(text)  # tokenization
        y = []
        for i in text:  # remove special characters
            if i.isalnum():
                y.append(i)
        text = y.copy()
        y.clear()
        for i in text:  # removing stopwords
            if i not in stopwords.words("english"):
                y.append(i)
        ps = PorterStemmer()  # for stemming
        text = y.copy()
        y.clear()
        for i in text:
            y.append(ps.stem(i))
        transformed_texts.append(" ".join(y))

    transformed_texts = np.array(transformed_texts)
    return np.array(transformed_texts)



