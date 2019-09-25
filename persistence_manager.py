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
        self.items_dict['id'] = self.items_dict['id'].astype(int)
        self.items_dict['original_title'] = map(lambda x: x.decode('utf-8','ignore'),self.items_dict['original_title'])
        self.items_dict = self.items_dict.sort_values('id')
        self.items_dict = self.items_dict.reset_index(drop=True)

        self.keywords_dict = pd.merge(self.keywords_dict,self.items_dict,on='id')
        self.keywords_dict = self.keywords_dict.sort_values('id')
        self.keywords_dict = self.keywords_dict.reset_index(drop=True)

    def __process_list(self,keys):
        return ','.join([i['name'].strip() for i in keys])[0:]

    def get_item(self,item_id):
    	item_founded = self.keywords_dict[self.keywords_dict['id'] == int(item_id)]

    	if not item_founded.empty:
            return item_founded
    	else:
    		return pd.DataFrame()

    def get_item_by_internal_id(self,index):
        return self.keywords_dict.iloc[index]['original_title']



