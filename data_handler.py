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
        df = self.process_prices(df,window=1)
        df = df.apply(lambda x: self.process_row(x) ,axis=1)
        print("Finished processing data")
        return df

    def process_row(self,row):
        """
            Takes a row, applies search for each source, and returns row
        """
        for source in self.sources:
            col_name = "raw_text_{}".format(source.name)

            if col_name in row.index and row[col_name] != "":
                continue
        
            row[col_name] = source.search(row["name"],date=row["date"])

        print("Finished {}".format(row["date"]))

        return row

    def process_prices(self,df,window=1):
        """
            Calculates return and then applies smoothing
        """
        df["price"] = df["Close"].pct_change(periods=window)

        df["price"].fillna(0,inplace=True)

        return df

        

        
    


        

    