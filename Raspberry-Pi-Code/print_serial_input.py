import serial

ser = serial.Serial('/dev/ttyACM0',9600)

while True:
	read_serial = ser.readline()[:-2]
	print read_serial
	ser.write("1")
