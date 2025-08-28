from DataRetrieval.dal.interfacess.dal_interface import IData_loader
from DataRetrieval.dal.functions.db_connector import Conector

class Data_loader(IData_loader):

    def __init__(self):
        self.connector = Conector()
        self.connector.DBconnect()
        self.db = self.connector.db

    def get_all_data(self,col)->list:
        collection = self.db[col]
        return list(collection.find({},{'_id':0}))