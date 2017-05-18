import serial_communication as ser
import leaving_from_classroom_validation_step as confirm
import time
import pymongo
from pymongo import MongoClient

ser.init()

client = MongoClient()
db = client['STUDENT_INFO']
collection = db["id_student"]
collection2 = db["student_log"]

while(True):
	ID = ser.readID()
	if (len(ID) == 5):
		print ("ID: " + ID)
		# eventually the line below
		# will be replaced by this:
		# a = confirmID(ID)
		a = confirm.is_Match(ID, collection2)
		print(a)
		ser.sendConfirmation(a)
	else:
		print (ID)
