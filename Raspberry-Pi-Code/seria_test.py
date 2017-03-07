import serial

def main():

	r = "receiving"
	c = "confirming"
	status = r

	ser = serial.Serial('/dev/ttyACM0',9600)
	#s = ['0']
	
	while True:
		read_serial=ser.readline()[:-2]
		if (status == r and read_serial == "Sending data..."):
			print read_serial
			status = c
		elif (status == c and validateID(read_serial)):
			print read_serial + " is a valid ID\n"
			# send back confirmation here
			#ser.write(stuff)
			status = r
		elif (status == c):
			print read_serial + " is not a valid ID\n"
			status = r

def validateID(idToValidate):
	if (isinstance(idToValidate, basestring)):
		if (idToValidate == "77777"):
			return True
		else:
			return False
	else:
		print type(idToValidate)
		return False

if __name__ == "__main__":
	main()
