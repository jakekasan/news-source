from sources import guardian_lookup

import datetime as dt
from sqlalchemy.engine import Engine

# business-y keywords
keywords = ["business","brexit","bank of england","economy","interest rates","unemployment"]

def keywords_to_query(keywords):
    # for keyword in keywords:
    #     keyword.replace(" "," AND ")
    return " OR ".join(["({})".format(keyword.replace(" "," AND ")) for keyword in keywords])

#print(keywords_to_query(keywords))

def get_list_of_dates(start="01-01-2010",days=366):
    dates = []
    start_date = dt.datetime.strptime(start,"%d-%m-%Y")
    for i in range(days):
        date = start_date + dt.timedelta(days=i)
        #dates.append(date.strftime("%Y-%m-%d"))
        dates.append(date)
    return dates

def process_results(results):
    for item in results:
        print(len(item))

def get_day(date=None,page=None):
    results = []
    response = guardian_lookup(query=keywords_to_query(keywords),date_from=date,date_to=date,raw_response=True,debug=True,page=page)
    if response["response"] and response["response"]["results"]:
        results += response["response"]["results"]
    if response["response"] and response["response"]["currentPage"] and response["response"]["currentPage"] < response["response"]["pages"]:
        results += get_day(date=date,page=response["response"]["currentPage"]+1)
    return results

def get_articles():
    articles = []
    dates = get_list_of_dates(days=10)
    for date in dates:
        articles.append(get_day(date=date))
    process_results(articles)


        

get_articles()
#print(get_list_of_dates())