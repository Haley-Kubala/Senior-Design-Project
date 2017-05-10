import serial
import time

MESSAGES = ("---start---", "----end----", "sending data...", "77778", "77777")

def main():

	r = "receiving"
	c = "confirming"
	status = r

	ser = serial.Serial('/dev/ttyACM0',9600)
	
	ser.readline()
	
	while True:
		read_serial=ser.readline()[:-2]
		if (read_serial in MESSAGES):
			if (status == r and read_serial == "sending data..."):
				print read_serial
				status = c
			elif (status == c and validateID(read_serial)):
				print "\x1b[0;32m" + read_serial + "\x1b[0m is a valid ID"
				ser.write("1")
				status = r
			elif (status == c and not validateID(read_serial)):
				print "\x1b[0;31m" + read_serial + "\x1b[0m is not a valid ID"
				ser.write("0");
				status = r
			else:
				print read_serial
		else:
			print "\x1b[0;31mIgnoring \"" + read_serial + "\"\x1b[0m"

# this is just a placeholder function
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
