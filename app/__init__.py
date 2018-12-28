from flask import request, jsonify, abort, render_template

from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy

from instance.config import app_config
import datetime as dt
from dateutil import parser

db = SQLAlchemy()

def create_app(config_name="development"):
    app = FlaskAPI(__name__, instance_relative_config=True)
    conf = app_config[config_name]
    app.config.from_object(conf)
    app.config.from_pyfile("config.py")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    @app.route("/")
    def home():
        articles = [
            {
                "api_id":1,
                "api_webPublicationDate":"01-01-2001",
                "api_webTitle":"First article of the year"
            },
            {
                "api_id":2,
                "api_webPublicationDate":"02-01-2001",
                "api_webTitle":"Second article of the year"
            },
            {
                "api_id":3,
                "api_webPublicationDate":"03-01-2001",
                "api_webTitle":"Last article of the year"
            }
        ]
        #return jsonify(app_config)
        return render_template("content.html",articles=articles)
        #return "This will be a simple one-page app to view the table"

    @app.route("/search/",methods=["GET","POST"])
    def search():
        if request.method == "GET":
            return render_template("search.html")
        else:
            return render_template("content.html")

    # API Stuff
    @app.route("/articles/",methods=["GET","POST"])
    def articles():
        from app.models import Article

        # GET METHOD
        if request.method == "GET":
            date = request.args.get("date")
            if date:
                date = parser.parse(date)

                from_date = date
                to_date = from_date + dt.timedelta(days=1)

                raw_results = Article.query.filter(Article.date_published >= from_date).filter(Article.date_published < to_date).all()
                
                if len(raw_results) < 1:
                    # bad result

                    # TODO
                    #  - if we have no articles, fetch from the guardian API

                    return jsonify({
                        "success":False
                    })

                results = []
                for result in raw_results:
                    results.append({
                        "title":result.api_webTitle,
                        "text":result.article_text,
                        "date":result.date_published
                    })

                results = jsonify({
                    "results":results,
                    "success":True
                })

                return results
                
                
                #return "{}".format(type(thing))
                # return "Got an actual date! {}".format(date)
        return "Bad request"

    return app