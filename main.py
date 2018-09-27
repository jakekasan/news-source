from data_handler import Data_Handler
from news_wrangler import News_Wrangler
from guardian import Guardian
from config import config
import datetime as dt
import pandas as pd
import numpy as np

def main():
    guardian = Guardian()

    df = pd.read_csv("./data/RBS.csv")

    print(df.head())

    df["date"] = df["Date"].apply(lambda x: dt.datetime.strptime(x,"%Y-%M-%d"))

    print(df.head())

    df["name"] = df.apply(lambda x: "RBS",axis=1)

    dh = Data_Handler()

    results = dh.run(df)

    print(results)

if __name__ == '__main__':
    main()