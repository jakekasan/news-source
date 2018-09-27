import datetime as dt
import requests
from config import config

class News_Wrangler:
    """
        Gets raw news string from news source
    """
    def __init__(self):
        return

    def search(self,search=None,date=None):
        """
            Prepare dates
        """

        if not date:
            date = dt.date.today()
        
        to_date = "{}-{}-{}".format(date.year,date.month,date.day)

        date = date - dt.timedelta(days=10)

        from_date = "{}-{}-{}".format(date.year,date.month,date.day)

        return self.api_search(search=search,from_date=from_date,to_date=to_date)

    def api_search(self,search=None,from_date=None,to_date=None):
        return

        
        

        
        