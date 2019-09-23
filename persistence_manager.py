import pandas as pd
from ast import literal_eval

class PersistenceManager:

    def __init__(self):
        self.keywords_dict = pd.read_csv('resources/keywords.csv')
        self.keywords_dict.keywords = map(lambda x: x.decode('utf-8','ignore'),self.keywords_dict.keywords)
        self.keywords_dict.keywords = self.keywords_dict.keywords.apply(literal_eval)
        self.keywords_dict['cleaned_keywords'] = self.keywords_dict.keywords.apply(self.__process_list)
        del self.keywords_dict['keywords']

        self.items_dict = pd.read_csv('resources/titles.csv')
        self.items_dict['id'] = self.items_dict['id'].apply(pd.to_numeric,errors='coerce')
        self.items_dict = self.items_dict.dropna()
        self.items_dict = self.items_dict['id'].astype(int)

    def __process_list(self,keys):
        return ','.join([i['name'] for i in keys])[0:]

    def get_item_name(self,item_id):
    	item_founded = self.items_dict[self.items_dict['id'] == int(item_id)]

    	if not item_founded.empty:
    		return item_founded.original_title[0]
    	else:
    		return ''


