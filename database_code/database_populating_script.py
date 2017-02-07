import pymongo
from pymongo import MongoClient

client = MongoClient()

#(1)establish connection to database
#(2)create dictionary for each individual student in the for loop
#(3)open and parse text tile(.split?)
#(4)get name, initials, dob, etc and store it in the dictionary
#(5)somehow send the individual student dictionaries to the mongodb
