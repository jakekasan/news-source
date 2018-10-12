import datetime as dt

def get_date_range(date=None,date_range=3):
    """
        takes a date (string)
        
        returns date_from, date_to
    """
    if date is None:
        date = dt.datetime.now()

    #if type(date) != dt.datetime:
        #date = dt.datetime.strptime(date)

    if type(date) == str:
        date = dt.datetime.strptime(date,"%Y-%m-%d")

    date_to = date
    date_from = date_to - dt.timedelta(days=date_range)

    return date_from,date_to

def get_date_pair_from_str(date_str=None,date_range=3):
    return get_date_range(date=dt.datetime.strptime(date_str,"%Y-%m-%d"),date_range=date_range)
    


