"""
    Find a way of importing a dynamic amount of sources
"""

#from sources.guardian import Guardian
#from sources import all_sources
from sources import all_sources
from tools import get_date_range

import datetime as dt
import pandas as pd


def single_lookup(query=None,date_from=None,date_to=None,articles=False,day_range=3):
    """
        returns a single string of news articles based on the query and dates
        
        if array == True then it returns an array of the articles
    """
    if query is None:
        return None

    if date_from is None:
        if date_to is None:
            date_from = dt.datetime.now()
            date_to = dt.datetime.now()

    article_list = []

    for source in sources_list:
        s = source()
        article_list += s.single_lookup(query=query,date_from=date_from,date_to=date_to)

    if not articles:
        return articles


    

def range_lookup(query=None,df=None,articles=False,date_range=3):
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

    for key,item in all_sources.items():
        print(key,item)
    print(data)

if __name__ == '__main__':
    main()