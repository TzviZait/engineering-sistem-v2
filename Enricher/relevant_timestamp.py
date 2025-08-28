import re
from datetime import datetime




class Relevant_timestamp:

    @staticmethod
    def get_dates(text:str):
        dates = []
        match = re.findall(r'\d{4}-\d{2}-\d{2}', text)
        dates = [datetime.strptime( date , '%d-%m-%Y').date() for date in match]
        return dates
    
    @staticmethod
    def get_relevant_timestamp(text):
        dates =  Relevant_timestamp.get_dates()
        return max(dates) if dates else None