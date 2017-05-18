import serial_communication as ser
import time

ser.init()

while(True):
	ID = ser.readID()
	if (len(ID) == 5):
		print ("ID: " + ID)
		# eventually the line below
		# will be replaced by this:
		# a = confirmID(ID)
		a = (ID == "77777") or (ID == "11111")
		print(a)
		ser.sendConfirmation(a)
	else:
		print (ID)
