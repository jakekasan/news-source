"""
    Find a way of importing a dynamic amount of sources
"""

from sources.guardian import Guardian

class Manager():
    def __init__(self):
        pass

    def get_text(self,query=None,data_from=None,date_to=None):
        """
            returns a pd.Series with raw text from all the sources
        """
        pass

    def get_list_of_text(self):
        pass