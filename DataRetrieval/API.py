from DataRetrieval.dal.functions.data_loader import Data_loader
from fastapi import FastAPI

app = FastAPI()
dal = Data_loader()

@app.get("/tweets_antisemitic")
def read_root():
    return dal.get_all_data('tweets_antisemitic')

@app.get("/tweets_not_antisemitic")
def read_root():
    
    return dal.get_all_data('tweets_not_antisemitic')
