import datetime as dt

def get_date_range(date=None,range=3):
    """
        takes a date (string or datetime object) and returns date_from and date_to
    """
    if date is None:
        date = None

    