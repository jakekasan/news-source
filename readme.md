# News Source

## About

This module helps maintain a local DB for articles which are to be used for NLP stuff. Runs a flask server.

## How to use

### Set environment variables

```bash
export FLASK_APP="run.py"
export APP_SETTINGS="development"
export SQLALCHEMY_DATABASE_URI="/path/to/database"
```

### run server

```bash
flask run
```

### Accessing server

The server runs on localhost:5000 by default, GET requests to /articles with a 'date' param search the database for articles on that day. If none are found, the server makes a call to the guardian API for the specific date (to be implemented...)

## To-Do

- [ ] Make it possible to get articles by date range rather than single date
- [ ] Instead of SQLite, use HDFS for storage