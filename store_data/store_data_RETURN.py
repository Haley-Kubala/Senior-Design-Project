#connect to mongo database
#connect to mongo collection
#create new document in collection
import argparse
import collections
import datetime
from datetime import date
#import mongodb
import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client['STUDENT_INFO']
collection = db["id_student"]

def main(args):
    end_date_time = datetime.datetime.now()
    ID = args["ID"]
    beginning_timestamp = args["beginning_timestamp"]
    if(find_id(collection)):
        return find_id
    else:
        print "no document"


def find_id(collection_name):
    '''
    If specified ID is in the collection the find_one function
    will return it.
    '''
    id_entry = collection_name.find_one({'id' : args["ID"]})
    return id_entry


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("ID", help="student ID needs to be entered")
    parser.add_argument("beginning_timestamp", help="taken from annies script")
    args = vars(parser.parse_args())
    main(args)
