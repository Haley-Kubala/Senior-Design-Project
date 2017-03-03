import serial
import time

serial = serial.Serial('/dev/ttyACM0',9600)
s = [0,1]

time.sleep(100)

while True:
	read_serial=serial.readline()
	s[0] = str(int(serial.readline(),16))
	print s[0]
	print read_serial
	#time.sleep(2)
	#serial.write(s[0])
	time.sleep(0.05)
