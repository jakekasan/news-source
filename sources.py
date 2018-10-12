"""
    sources.py
"""

import os
import sys
import requests

def config(source=None):
    """
        looks for file with API keys
    """

    # take 
    if source is None:
        return None

    if "api.keys" not in os.listdir():
        return None

    with open("./api.keys","r") as f:
        raw_lines = f.readlines()

        api_keys = {}
        for line in raw_lines:
            data = line.split(":")
            name, key = data[0], data[1]
            api_keys[name] = key

        if source in api_keys.keys():
            return api_keys[source]
        return None
        
        



def guardian_lookup(query=None,date_from=None,date_to=None,raw_response=False,debug=False):
    """
        returns a list of articles for the given query, date_from, date_to
    """
    key = config(source="guardian")

    if key is None:
        # maybe raise an error
        print("API_key not found in config")
        raise Exception("API key for {} was not found.\nPlease format api.keys file like so: [name of source]:[api key]")

    date_from = date_from.strftime("%Y-%m-%d")
    date_to = date_to.strftime("%Y-%m-%d")

    params = {
        "q":query,
        "from-date":date_from,
        "to-date":date_to,
        "api-key":key,
        "show-fields":"bodyText",
        "page-size":50
    }

    guardian_address = "https://content.guardianapis.com/search"

    r = requests.get(guardian_address,params=params)

    if debug:
        print(r.url)

    data = r.json()

    if raw_response:
        return data

    if "response" in data.keys():

        if "results" in data["response"]:

            articles = data["response"]["results"]
            return list(map(lambda x: x["fields"]["bodyText"],articles))

        return []
        
    return []



all_sources = {
    "guardian":guardian_lookup
}