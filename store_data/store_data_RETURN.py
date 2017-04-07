#connect to mongo database
#connect to mongo collection
#create new document in collection
#adjust script so it takes ID and Timestamp as args
import argparse
import collections
import datetime
from datetime import date
import mongodb
import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client['STUDENT_INFO']
collection = db["id-student"]

def main(args):

    end_date_time = datetime.datetime.now()
    ID = args["ID"]
    beginning_timestamp = args["beginning_timestamp"]

def find_id(collection_name):
    id_entry = collection_name.find_one({'ID' : id},)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("ID", help="student ID needs to be entered")
    parser.add_argument("beginning_timestamp", help="taken from annies script")
    args = vars(parser.parse_args())
    main(args)
