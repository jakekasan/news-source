import pandas as pd

from guardian import Guardian

source_wranglers = {
    "guardian":Guardian
}

class Data_Handler:
    def __init__(self,df=None,sources=["guardian"]):
        self.df = df
        self.sources = [source_wranglers[x]() for x in sources]

    def run(self,df=None):
        print("Started processing data for {}".format(df["name"][0]))
        print("Df size:",df.shape)
        df = df.apply(lambda x: self.process_row(x) ,axis=1)
        print("Finished processing data")
        return df

    def process_row(self,row):
        results = ""

        for source in self.sources:
            text = source.search(row["name"],date=row["date"])
            results = "".join([results,text])

        row["raw_text"] = results

        print("Finished {}".format(row["date"]))

        return row


        

    