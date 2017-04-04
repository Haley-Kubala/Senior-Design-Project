#connect to mongo database
#connect to mongo collection
#create new document in collection
#adjust script so it takes ID and Timestamp as args
import argparse
import datetime
from datetime import date
import time
#import collections
#import mongodb
#import pymongo
#from pymongo import MongoClient


def main(args):
    end_date_time = datetime.datetime.now()
    print args


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("ID", help="student ID needs to be entered")
    parser.add_argument("beginning_timestamp", help="taken from annies script")
    args = vars(parser.parse_args())
    main(args)


'''with open('leave_info_file') as leave_info_file:
    ID_leave_time_stamp = leave_info_file.read()
    info_list = ID_leave_time_stamp.split(" ")
    ID = info_list[1]
    date = info_list[2]
    time = info_list[3]
'''
