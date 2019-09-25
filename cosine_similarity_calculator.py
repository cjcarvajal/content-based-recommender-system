from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import sent_tokenize

class CosineSimilarityCalculator:

	def __init__(self,corpus_df):
		self.corpus = corpus_df.copy()
		self.corpus.set_index('id',inplace=True)
		self.corpus.sort_index(inplace=True)
		self.corpus_list = self.corpus.cleaned_keywords.tolist()
		self.corpus_list = [w.decode('utf-8','ignore') for w in self.corpus_list]

		custom_vec = CountVectorizer(tokenizer=self.__custom_tokenizer)
		self.item_matrix = custom_vec.fit_transform(self.corpus_list)
		self.cosine_matrix = cosine_similarity(self.item_matrix,self.item_matrix)

	def __custom_tokenizer(self,s):
		return s.split(',')

	def get_similar_items(self,id,number_of_items):
		return self.cosine_matrix[id].argsort()[:-number_of_items:-1]