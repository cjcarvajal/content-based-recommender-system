from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import sent_tokenize

corpus = [
  'the, brown fox, jumped over the brown dog',
  'the, quick, brown fox',
  'the, brown brown dog',
  'the, fox ate the dog'
]

def my_tokenizer(s):
    return s.split(',')

custom_vec = CountVectorizer(tokenizer=my_tokenizer)
wm = custom_vec.fit_transform(corpus)
