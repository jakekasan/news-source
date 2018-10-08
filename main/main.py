"""
    Find a way of importing a dynamic amount of sources
"""

#from sources.guardian import Guardian
#from sources import all_sources
import sources
import datetime as dt


def single_lookup(query=None,date_from=None,date_to=None,array=False):
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


    

def range_lookup(query=None,df=None):
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

def main():
    print(sources.Guardian)

if __name__ == '__main__':
    main()