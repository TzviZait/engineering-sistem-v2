
from splitter import Splitter

from dal import DAL

import time
dal = DAL()

splitter = Splitter()
skip = 0
while True:
    data = dal.get_database(skip)
    skip += 100
    splitter.splitter(data)
    time.sleep(1)



