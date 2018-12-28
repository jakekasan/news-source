#!/bin/bash

# custom variables

export FLASK_APP="run.py"
export FLASK_ENV="development"
export SECRET="my little donkey"
export SQLALCHEMY_DATABASE_URI="sqlite:///./articles.db"