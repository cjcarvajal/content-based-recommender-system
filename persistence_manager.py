import pandas as pd
from ast import literal_eval

class PersistenceManager:

    def __init__(self):
        self.keywords_dict = pd.read_csv('./resources/keywords.csv')
        self.keywords_dict.keywords = self.keywords_dict.keywords.apply(literal_eval)
        self.keywords_dict['cleaned_keywords'] = self.keywords_dict.keywords.apply(self.__process_list)
        del self.keywords_dict['keywords']
        self.corpus = self.keywords_dict.cleaned_keywords.tolist()

    def __process_list(self,keys):
        return ','.join([i['name'] for i in keys])[0:]
