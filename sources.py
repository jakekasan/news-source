"""
    sources.py
"""

import os
import sys

def config(source=None):
    """
        looks for file with API keys
    """

    # take 
    if source is None:
        return None

    if "api.keys" not in os.listdir():
        return None

    with open("api.keys","w") as f:
        raw_lines = f.readlines()

        api_keys = {}
        for line in raw_lines:
            data = line.split(":")
            name, key = data[0], data[1]
            api_keys[name] = key

        if source in api_keys.keys():
            return api_keys[source]
        return None
        
        



def guardian_lookup(query=None,date_from=None,date_to=None):
    """
        returns a list of articles for the given query, date_from, date_to
    """
    key = config(source="guardian")

    if key is None:
        return None

    
