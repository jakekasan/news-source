from data_handler import Data_Handler
from news_wrangler import News_Wrangler
from guardian import Guardian
from config import config
from ticker_lookup import ticker_lookup

import datetime as dt
import numpy as np
import os
import pandas as pd
import re



def main():

    pwd = os.getcwd()

    if "data" not in [x for x in os.listdir(pwd) if os.path.isdir(x)]:
        print("No data directory")
        return

    data_dir = os.path.join(pwd,"data")

    csv_regex = re.compile(r".*\.csv")

    for f in os.listdir(data_dir):
        match = csv_regex.search(f)
        print(match.group())
    return
    #ticker_lookup("RBS")
    return

    df = pd.read_csv("./data/RBS.csv")

    print(df.head())

    df["date"] = df["Date"].apply(lambda x: dt.datetime.strptime(x,"%Y-%M-%d"))

    print(df.head())

    df["name"] = df.apply(lambda x: "RBS",axis=1)

    df = df.head(20)

    dh = Data_Handler()

    results = dh.run(df)

    print(results.tail(1)["raw_text_guardian"].values)

if __name__ == '__main__':
    main()