from pymongo import MongoClient
import os

def load_data_to_mongo(df):
    """ Carga la información a Atlas """
    uri = os.environ["MONGO_URI"]
    client =  MongoClient("")

    db = client['irc_pp_panels']
    collection = db['panels_info']

    df.reset_index(inplace=True)
    data_dict = df.to_dict("records")
    # Insert collection
    collection.insert_many(data_dict)