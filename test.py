from pymongo import MongoClient
import pymongo
import pandas as pd
import numpy as np

client = MongoClient()  # mongodb server
db = client['xfd_db']
df = db['xfd_veg_price']
#xfd_veg_price = client.xfd_db.xfd_veg_price
#x=db.getCollection('xfd_veg_price').find({"date":{$gte:"2019-01-01"}})
#xfd_veg_price.find({"date":{$gte:"2019-01-01"}})
data = pd.DataFrame(list(df.find()))

writer = r"D:\Desktop\test.csv"
data.to_csv(writer, index=False)
