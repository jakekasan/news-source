from config import config
import requests
from news_wrangler import News_Wrangler

address = "https://content.guardianapis.com/search"

class Guardian(News_Wrangler):
    def __init__(self):
        super()
        self.name = "guardian"
        self.address = config["sources"]["guardian"]["address"]
        self.API_KEY = config["sources"]["guardian"]["API_KEY"]

    def api_search(self,search,from_date=None,to_date=None):
        """
            API-specific search function

            returns text
        """

        params = {
            "api-key":self.API_KEY,
            "q":search,
            "from-date":from_date,
            "to-date":to_date,
            "show-fields":"bodyText",
            "tags":"business"
        }

        try:
            r = requests.get(self.address,params=params)
            results = r.json()

            articles = results["response"]["results"]

            return self.process_result(articles)

        except:
            return ""

    def process_result(self,results):
        """
            Takes the results from the API and processes them to a single string
        """
        try:
            if len(results) < 1:
                return ""

            all_text = ""

            for article in results:
                all_text = "".join([article["fields"]["bodyText"],all_text])

            return all_text

        except:
            return ""