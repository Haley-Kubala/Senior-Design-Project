import argparse
import pymongo
from pymongo import MongoClient

#specifiy port later
client = MongoClient()
db = client.test_database
collection = db.test_collection


def fill_dict():
    studentDict = {}
    #take text file as a parameter
    #go through file, line by line, break on spaces and store
    #each section as a variable
    #add each part to the dictionary
    #return dictionary

parser = argparse.ArugmentParser()
parser.add_argument("file", help="enter path to a text file")
args = parser.parse_args()

#(1)establish connection to database
#(2)create dictionary for each individual student in the for loop
#(3)open and parse text tile(.split?)
#(4)get name, initials, dob, etc and store it in the dictionary
#(5)somehow send the individual student dictionaries to the mongodb
