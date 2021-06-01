import serial
ser = serial.Serial('COM77', 115200,stopbits=1,bytesize=8, timeout=0, rtscts=1)
ser.flushInput()

print("Waiting for data to come...")
while True:
	serial_out = ser.readline().decode('ascii')
	if serial_out:
		print(serial_out)
