# module imports
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, DateTime, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# local imports
from app import db

class Article(db.Model):

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

    def save(self):
        db.session.add(self)
        db.session.commit()

    # def get_all_dates(self):
    #     return [x for x in self.query.distinct("date_published")]

    @staticmethod
    def get_all():
        return Article.query.all()


    def __repr__(self):
        return f"<Article: {self.date_published}, {self.api_webTitle}"
    



# Base = declarative_base()

# class Article(Base):

#     __tablename__ = "articles"

#     id = Column(Integer,primary_key=True)
#     api_id = Column(String)
#     api_type = Column(String)
#     api_sectionId = Column(String)
#     api_sectionName = Column(String)
#     api_webPublicationDate = Column(String)
#     api_webTitle = Column(String)
#     api_webUrl = Column(String)
#     api_apiUrl = Column(String)
#     api_isHosted = Column(Boolean)
#     api_pillarId = Column(String)
#     api_pillarName = Column(String)
#     article_text = Column(String)
#     date_retrieved = Column(DateTime)
#     date_published = Column(DateTime)