"""
    Find a way of importing a dynamic amount of sources
"""

from sources.guardian import Guardian

class Manager():
    def __init__(self):
        pass

    def single_lookup(self,query=None,date_from=None,date_to=None,array=False):
        """
            returns a single string of news articles based on the query and dates
            
            if array == True then it returns an array of the articles
        """

    def range_lookup(self,query=None,df=None):
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

        # Do the magic

    def get_text(self,query=None,data_from=None,date_to=None):
        """
            returns a pd.Series with raw text from all the sources
        """
        pass

    def get_list_of_text(self):
        pass