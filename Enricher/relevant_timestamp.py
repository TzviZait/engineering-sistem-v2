import re
from datetime import datetime




class Relevant_timestamp:

    @staticmethod
    def get_dates(text:str):
        dates = []
        match = re.findall(r'\d{4}-\d{2}-\d{2}', text)
        dates = [datetime.strptime( date , '%d-%m-%Y').date() for date in match]
        return max(dates) if dates else None
    
    @staticmethod
    def get_relevant_timestamp(text):
        return ''
    

print(Relevant_timestamp.get_dates('&quot;Tomorrow (25-03-2020 09:30) we will attack using a gun (AK-47) near the border&quot;,'))