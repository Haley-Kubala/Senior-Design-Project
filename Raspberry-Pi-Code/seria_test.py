import serial

ser = serial.Serial('/dev/ttyACM0',9600)
s = [0,1]
while True:
	read_serial=ser.readline()
	s[0] = str(int (ser.readline(),16))
	print s[0]
	print read_serial
	time.sleep(2)
	ser.write(s[0])
	time.sleep(0.05)
