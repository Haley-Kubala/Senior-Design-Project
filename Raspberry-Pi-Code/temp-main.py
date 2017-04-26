import serial_communication as ser
import time

ser.init()

while(True):
	ID = ser.readID()
	print("ID: " + ID)
	if (len(ID) == 5):
		a = (ID == "77777")
		print(a)
		ser.sendConfirmation(a) 
