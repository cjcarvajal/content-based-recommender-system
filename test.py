import pandas as pd
from ast import literal_eval

keywords_dict = pd.read_csv('./resources/keywords.csv')

def process_list(keys):
    return ([i['name'] for i in keys])

keywords_dict.keywords = keywords_dict.keywords.apply(literal_eval)
keywords_dict['cleaned_keywords'] = keywords_dict.keywords.apply(process_list)
del keywords_dict['keywords']
print(keywords_dict)
