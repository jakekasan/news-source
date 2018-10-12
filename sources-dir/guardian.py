#from config.news_sources import guardian as api
import requests
from sources.news_wrangler import News_Wrangler

address = "https://content.guardianapis.com/search"

class Guardian(News_Wrangler):
    def __init__(self,debug=False):
        super()
        self.debug = debug
        self.name = "guardian"
        self.address = None #api["address"]
        self.api_key = None #api["API_KEY"]

    def set_api_address(self,address=None):
        self.address = address

    def set_api_key(self,key=None):
        self.api_key = key

    def api_search(self,search,from_date=None,to_date=None,news_delay=None,just_results=False):
        """
            API-specific search function

            returns raw text for this source
        """

        if news_delay is None:
            # reset to default
            news_delay = 3

        params = {
            "api-key":self.api_key,
            "q":"{} OR (royal AND bank AND of AND scotland) OR (brexit) OR (mark AND carney) OR economy OR unemployment OR".format(search),
            "from-date":from_date,
            "to-date":to_date,
            "show-fields":"bodyText",
            "tags":"business/business",
            "page-size":50
        }

        try:
            r = requests.get(self.address,params=params)
            results = r.json()

            if self.debug:
                print(r.url)

            articles = results["response"]["results"]

            if just_results:
                return articles

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


    def single_lookup(self,query=None,date_from=None,date_to=None):