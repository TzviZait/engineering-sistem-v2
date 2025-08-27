
from splitter import Splitter

from dal import DAL

import time
dal = DAL()

splitter = Splitter()

while True:
    data = dal.get_database()
    splitter.splitter(data)
    time.sleep(60)



