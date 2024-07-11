import time
from printrun.printcore import printcore
from printrun import gcoder
import serial

ser = serial.Serial('COM3', 9600)  # Example: COM port 3, baud rate 9600
# Sending a command
command = bytearray([0x02, 0x41, 0x00, 0x00, 0x00, 0x00, 0x03])
ser.write(command)

# Reading the response
response = ser.read(64)  # Reading 64 bytes from the device, as per your document
print(response)

# Connect to the printer
p = printcore('/dev/ttyUSB0', 115200)

# Wait for the printer to be ready
while not p.online:
    time.sleep(0.1)

# Send G-code commands
gcode = gcoder.LightGCode(["G28", "G1 X10 Y10 Z10"])
p.startprint(gcode)

# Optionally, monitor the print status
while p.printing:
    print(p.get_current_command())
    time.sleep(0.5)

# Close the connection
p.disconnect()
ser.close()
