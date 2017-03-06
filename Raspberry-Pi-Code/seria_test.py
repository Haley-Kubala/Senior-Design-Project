import serial

ser = serial.Serial('/dev/ttyACM0',9600)
s = ['0']
while True:
	read_serial=ser.readline()
	if (read_serial == "test"):
		a = 0
		# send back confirmation here
	print read_serial
