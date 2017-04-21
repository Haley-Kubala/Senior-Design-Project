
import argparse
import collections
import datetime
from datetime import date
import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client['STUDENT_INFO']
collection = db["id_student"]
collection2 = db["student_log"]


def find_id(collection_name, id_arg):
    '''
    If specified ID is in the collection the find_one function
    will return it.
    '''
    id_entry = collection_name.find_one({'id' : id_arg})
    return id_entry


def store_data(collection_name, id_args, leave_time, return_time):
    '''Takes input from annie's script and creates
    new mongo document in correct collection.
    '''
    document = db.collection_name.insert({"id": id_args},
                                        {"leave time" : leave_time},
                                        {"return time", return_time})
    return document


def main(args):
    end_date_time = datetime.datetime.now()
    ID = args["ID"]
    print ID
    beginning_timestamp = args["beginning_timestamp"]
    if(find_id(collection, ID)):
        store_data(collection2, ID, beginning_timestamp, end_date_time)
    else:
        print "no such document"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("ID", help="student ID needs to be entered")
    parser.add_argument("beginning_timestamp", help="taken from annies script")
    args = vars(parser.parse_args())
    main(args)
