import serial

r = "receiving"
c = "confirming"
status = r

ser = serial.Serial('/dev/ttyACM0',9600)
s = ['0']

while True:
	read_serial=ser.readline()[:-2]
	if (status == r and read_serial == "Sending data..."):
		print read_serial
		status = c
	if (status == c and read_serial == "77777"):
		print read_serial + " is a valid ID\n"
		# send back confirmation here
		#ser.write(stuff)
		status = r

def validateID(idToValidate):
	if (isinstance(idToValidate, basestring):
		if (idToValidate == "77777"):
			print idToValidate + " is a valid ID\n"
		else:
			print idToValidate + " is not a valid ID\n"
	else:
		print type(idToValidate)
