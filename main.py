import pyautogui
import time 
import serial

arduinoSerial = serial.Serial(port="port", baudrate=9600)
time.sleep(1)

while True:
   data = str(arduinoSerial.readline()) # get serial port data
   axis = data.split(",") # read the axis data
   (X,Y) = pyautogui.position() # read the current position of cursor
   x = int((axis[0].split("'"))[1]) # X-axis joystick
   y = int(axis[1]) # Y-axis joystick
   z = axis[2] # button click
   pyautogui.moveTo(X + x, Y - y) # move cursor
   print(x, y, z)