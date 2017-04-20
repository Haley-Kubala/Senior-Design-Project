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


def find_id(collection_name, id_arg):
    '''
    If specified ID is in the collection the find_one function
    will return it.
    '''
    #check if this is how you find a document also figure out
    #how to make function understand what args is
    id_entry = collection_name.find_one({'id' : id_arg})
    return id_entry


def main(args):
    end_date_time = datetime.datetime.now()
    ID = args["ID"]
    print ID
    beginning_timestamp = args["beginning_timestamp"]
    if(find_id(collection, ID)):
        print find_id(collection, ID)
    else:
        print "no such document"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("ID", help="student ID needs to be entered")
    parser.add_argument("beginning_timestamp", help="taken from annies script")
    args = vars(parser.parse_args())
    main(args)
