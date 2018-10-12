"""
    Find a way of importing a dynamic amount of sources
"""

#from sources.guardian import Guardian
#from sources import all_sources
from sources import all_sources
from tools import get_date_range, get_date_pair_from_str

import requests
import re
import datetime as dt
import pandas as pd
import test

def single_lookup(query=None,date=None,articles=False,date_range=3,by_source=False):
    """
        returns a single string of news articles based on the query and dates
        
        if array == True then it returns an array of the articles
    """
    if query is None:
        return None

    if date is None:
        date = dt.datetime.now()

    date_from,date_to = get_date_range(date=date,date_range=date_range)

    article_dict = {}

    for key,source in all_sources.items():
        article_dict[key] = source(query=query,date_from=date_from,date_to=date_to)

    article_list = [x for x in article_dict.values()]

    if not articles:
        if by_source:
            return article_dict
        return "".join(article_list)
        
    return article_list

    
def range_lookup(query=None,df=None,article_list=True,date_range=3,date_col="Date"):
    """
        takes a pandas dataframe and returns it with a one column per source

        params:
            query: string, the search query, default = None
            df: pandas DataFrame, the data frame to which results will be appended
            articles: bool, 
    """
    if query is None:
        """
            maybe raise?
        """
        return None

    if df is None:
        """
            maybe raise?
        """
        return None

    if date_col not in df.columns:
        """
            maybe raise?
        """
        return None

    df[date_col] = df[date_col].apply(lambda x: dt.datetime.strptime(x,"%Y-%m-%d"))

    # Do the magic

    def get_results_for_row(row,query=None,source=None):
        date_from,date_to = get_date_range(date=row[date_col],date_range=date_range)

        articles = source(query=query,date_from=date_from,date_to=date_to)
        if article_list:
            return articles
        else:
            return "".join(articles)
        
        
    for key,item in all_sources.items():
        df["{}_article_list".format(key)] = df.apply(lambda x: get_results_for_row(row=x,query=query,source=item),axis=1)

    return df

def main():
    test.run_tests()
    #df = pd.read_csv("./data/RBS.csv")
    #data = df.sample(10)

    #results = single_lookup(query="RBS",by_source=True)
    #results = range_lookup("RBS",df=data,articles=True,date_range=3)
    #print(results.head())
    #results.apply(lambda x: print(len(x["guardian_article_list"])),axis=1)
    #results.to_csv("./results.csv")

    # testing guardian API

    # params = {
    #     "q":"RBS OR (Royal AND Bank AND of AND Scotland) OR Brexit OR (Bank AND Of AND England) OR Chancellor OR Unemployment OR inflation OR bank",
    #     "from-date":"2017-10-10",
    #     "to-date":"2017-10-13",
    #     "api-key":"c02f338f-9587-4500-b9b9-06351534443a",
    #     "show-fields":"bodyText",
    #     "page-size":100,
    #     "tag":"business/business"
    # }

    # guardian_address = "https://content.guardianapis.com/search"

    # r = requests.get(guardian_address,params=params)

    # data = list(map(lambda x: x["webTitle"] ,r.json()["response"]["results"]))

    # print(len(data))

if __name__ == '__main__':
    main()