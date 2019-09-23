from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import sent_tokenize

class CosineSimilitudeCalculator:

	def __init__(self,corpus):
		corpus.set_index('id',inplace=True)
		corpus.sort_index(inplace=True)
		corpus = corpus.cleaned_keywords.tolist()
		corpus = [w.decode('utf-8','ignore') for w in corpus]

		custom_vec = CountVectorizer(tokenizer=self.__custom_tokenizer)
		self.item_matrix = custom_vec.fit_transform(corpus)
		self.cosine_matrix = cosine_similarity(self.item_matrix,self.item_matrix)

	def __custom_tokenizer(self,s):
		return s.split(',')

	def get_similar_items(self,id,number_of_items):
		return self.cosine_matrix[id].argsort()[:-number_of_items:-1]

'''
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
print (wm.toarray())
'''