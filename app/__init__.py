from flask import request, jsonify, abort

from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy

from instance.config import app_config
import datetime as dt
from dateutil import parser

db = SQLAlchemy()

def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile("config.py")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    @app.route("/articles/",methods=["GET","POST"])
    def articles():
        from app.models import Article
        if request.method == "GET":
            date = request.args.get("date")
            if date:
                all_articles = Article.query.distinct(Article.date_published).all()

                date = parser.parse(date)

                for article in all_articles:
                    article_date = article.date_published
                    to_date = article_date + dt.timedelta(days=1)

                    if date.year == article_date.year and date.month == article_date.month and date.day == article_date.day:
                        raw_results = Article.query.filter(Article.date_published >= article_date).filter(Article.date_published < to_date)
                        results = []
                        for result in raw_results:
                            results.append({
                                "title":result.api_webTitle,
                                "text":result.article_text,
                                "date":result.date_published
                            })
                        results = jsonify(results)
                        return results
                return "I do not have this date."
                
                #return "{}".format(type(thing))
                # return "Got an actual date! {}".format(date)
        return "Bad request"

    return app