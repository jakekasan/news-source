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

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()




def get_articles_by_date(date=None):
    return session.query(Article).filter_by(date_published=date).all()


date = dt.datetime(2014,12,12)

articles = get_articles_by_date(date=date)

for art in articles:
    print(art.api_webTitle)

session.close()