import serial

ini = False
ser = serial.Serial('/dev/ttyACM0', 9600)

def init():
        ser = serial.Serial('/dev/ttyACM0', 9600)
        ini = True

def sendConfirmation(confirm):
        if (not(ini)):
                init()
        if (isinstance(confirm, bool)):
                if (confirm):
                        ser.write("1")
                else:
                        ser.write("0")
        elif (isinstance(confirm, int)):
                if (confirm == 1):
                        ser.write("1")
                else:
                        ser.write("0")

def readID():
        if (not(ini)):
                init()
        return ser.readline()[:-2]

def available():
	if (not(ini)):
		init()
	return 
