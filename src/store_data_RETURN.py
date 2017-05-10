
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
    :param collection_name: the name of the student_id collection_name
                            which stores student name to student id
    :param id_arg: this is the id that we want to check if it exists
                   in the student_id database.
    :return: it returns id_entry which is a variable that contains
            the mongo command that finds the specific id in the collection
    '''
    id_entry = collection_name.find_one({'id' : id_arg})
    return id_entry


def store_data(collection_name, id_args, leave_time, return_time):
    '''Takes input from annie's script and creates
    new mongo document in correct collection.
    :param collection_name: the name of the mongo collection where we want
                            to store the information. this is specificaly
                            the student_log collection.
    :param id_args: this is the id we want to store in the student_log collection
                    it comes from args["ID"].
    :param leave_time: this is the time that the student leaves the classroom
                       this comes from arg parse and is specifically args["beginning_timestamp"].
    :param return_time: this is the datetime object that we generate in this script
    :return: this returns nothing and is just a mongo command
    '''
    collection_name.insert({"id": id_args,
                                "leave_time" : leave_time,
                                "return_time" : return_time})


def main(args):
    '''
    Main creates the return time and then calls the store_data() function
    with the args from argparse. It assigns variables to the id Argument
    and the beginning_timestamp argument.
    :param args: args["ID"] and args["beginning_timestamp"]
    :return: this returns nothing it just runs the store_data() function
    '''
    end_date_time = datetime.datetime.now()
    student_id = args["ID"]
    beginning_timestamp = args["beginning_timestamp"]
    store_data(collection2, student_id, beginning_timestamp, end_date_time)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("ID", help="student ID needs to be entered")
    parser.add_argument("beginning_timestamp", help="taken from annies script")
    args = vars(parser.parse_args())
    main(args)
