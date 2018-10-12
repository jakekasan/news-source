"""
    Find a way of importing a dynamic amount of sources
"""

#from sources.guardian import Guardian
#from sources import all_sources
from sources import all_sources
from tools import get_date_range

import datetime as dt
import pandas as pd


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

    


    

def range_lookup(query=None,df=None,articles=True,date_range=3):
    """
        returns a pd.Series of results for a range of dates for the given query
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

    if "date" not in df.columns:
        """
            maybe raise?
        """
        return None

    # Do the magic

    def get_results_for_row(row,query=None,source=None):
        date_to = row["date"]
        date_from = date_to - dt.timedelta(days=date_range)

        return source(query=query,date_from=date_from,date_to=date_to)
        
        

    for key,item in all_sources.items():
        df["{}_article_list".format(key)] = df.apply(lambda x: get_results_for_row(row=x,query=query,source=item),axis=1)

    return df




    

def main():

    df = pd.read_csv("./data/RBS.csv")
    data = df.sample(10)

    results = single_lookup(query="RBS",by_source=True)
    print(results)

if __name__ == '__main__':
    main()