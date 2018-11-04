from sources import guardian_lookup
import time
import datetime as dt
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, DateTime, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

db_url = "sqlite:////Users/jakubkasan/coding/news-source/articles.db"
engine = create_engine(db_url)
Base = declarative_base()

class Article(Base):

    __tablename__ = "articles"

    id = Column(Integer,primary_key=True)
    api_id = Column(String)
    api_type = Column(String)
    api_sectionId = Column(String)
    api_sectionName = Column(String)
    api_webPublicationDate = Column(String)
    api_webTitle = Column(String)
    api_webUrl = Column(String)
    api_apiUrl = Column(String)
    api_isHosted = Column(Boolean)
    api_pillarId = Column(String)
    api_pillarName = Column(String)
    article_text = Column(String)
    date_retrieved = Column(DateTime)
    date_published = Column(DateTime)
    
Base.metadata.create_all(bind=engine)

# business-y keywords
keywords = ["business","brexit","bank of england","economy","interest rates","unemployment"]

def keywords_to_query(keywords):
    # for keyword in keywords:
    #     keyword.replace(" "," AND ")
    return " OR ".join(["({})".format(keyword.replace(" "," AND ")) for keyword in keywords])

#print(keywords_to_query(keywords))

def get_list_of_dates(start="01-11-2010",days=366):
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
    print("Keys")
    print(results[0][0].keys())
    for value in results[0][0].values():
        print(type(value))

def add_day_to_db(articles,date_published=None,session=None):
    """
        Adds the articles to the sql database
    """
    if articles == []:
        return

    for article in articles:
        data = {"api_{}".format(a):b for a,b in article.items() if a != "fields"}
        data["article_text"] = article["fields"]["bodyText"]
        data["date_retrieved"] = dt.datetime.now()
        data["date_published"] = date_published

        art = Article(**data)
        session.add(art)
    session.commit()

def get_day(date=None,page=None):
    results = []
    time.sleep(0.1)
    response = guardian_lookup(query=keywords_to_query(keywords),date_from=date,date_to=date,raw_response=True,debug=True,page=page)
    if response["response"] and response["response"]["results"]:
        results += response["response"]["results"]
    if response["response"] and response["response"]["currentPage"] and response["response"]["currentPage"] < response["response"]["pages"]:
        results += get_day(date=date,page=response["response"]["currentPage"]+1)
    return results

def get_articles(start="23-10-2011",days=365,session=None):
    dates = get_list_of_dates(start=start,days=days)
    for date in dates:
        print(f"Getting articles for {date}...",end=" ",flush=True)
        articles = get_day(date=date)
        add_day_to_db(articles,date_published=date,session=session)
        print("done")
    print(f"Last date processed: {dates[-1]}")
    print("Finished all!")


Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

get_articles(start="2-1-2014",days=(365*3)+1,session=session)

session.close()
#print(get_list_of_dates())