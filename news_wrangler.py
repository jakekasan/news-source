import datetime as dt
import requests


class News_Wrangler:
    def __init__(self,address,API_KEY):
        self.save_location = None
        self.address = address
        self.API_KEY = API_KEY
        return


    def search(self,search=None,date="2012-10-9"):
        """
            Run a search for the query on the API
        """

        # if not date:
        #     t = dt.date.today()
        #     date = "{}-{}-{}".format(t.year,t.month,t.day)
        #     print("Date:",date)

        params = {
            "api-key":self.API_KEY,
            "q":search,
            "from-date":"2012-10-9",
            "to-date":"2013-10-10"
        }

        r = requests.get(self.address,params=params)
        results = r.json()

        for result in results["response"]:
            if result != "result":
                print(result)
        
        for item in results["response"]["results"]:
            print(item,"\n")

    def set_save_location(self,location):
        self.save_location = location