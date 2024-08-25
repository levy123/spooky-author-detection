import pandas as pd
import nltk
from nltk.corpus import stopwords
nltk.download("stopwords")
from nltk.tokenize import word_tokenize
import re
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
nltk.download("punkt")
nltk.download("wordnet")
nltk.download("omw-1.4")

## Preprocessing function

def remove_punctuation(text):
    tokens = word_tokenize(text)
    non_word_list = ["th", 'h', 'w']
    word_tokens = [re.sub(r'[^\w\s]', '', word) for word in tokens if re.sub(r'[^\w\s]', '', word) and word not in non_word_list]
    return word_tokens

def lemmatize_text(tokens):
    lemmatizer = WordNetLemmatizer()
    # Lemmatize each word
    lemmatized_tokens =[lemmatizer.lemmatize(token) for token in tokens]
    return lemmatized_tokens


def untokenize(tokens):
    return ' '.join(tokens)

stop_words = set(stopwords.words("english"))