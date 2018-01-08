import time
from time import gmtime, strftime
import RPi.GPIO as GPIO

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import Adafruit_DHT

# setting a current mode
GPIO.setmode(GPIO.BCM)
#removing the warings
GPIO.setwarnings(False)
#creating a list (array) with the number of GPIO's that we use
pins = [13,19,26]
#setting the mode for all pins so all will be switched on
GPIO.setup(pins, GPIO.OUT, initial=GPIO.HIGH)

ans=True 
while ans:
	print ("""
	1.Liga/Desl luz 1
	2.Liga/Desl luz 2
	3.Liga/Desl bomba
	4.Exit/Quit
	""")
	ans=raw_input("What would you like to do? ") 
	if ans=="1": 
		if GPIO.input(13)==1:
			GPIO.output(13,  GPIO.LOW)
		elif GPIO.input(13)==0:
			GPIO.output(13,  GPIO.HIGH)
	elif ans=="2":
		if GPIO.input(19)==1:
			GPIO.output(19,  GPIO.LOW)
		elif GPIO.input(19)==0:
			GPIO.output(19,  GPIO.HIGH)
	elif ans=="3":
		if GPIO.input(26)==1:
			GPIO.output(26,  GPIO.LOW)
                elif GPIO.input(26)==0:
                        GPIO.output(26,  GPIO.HIGH)
	elif ans=="4":
		print("\n Goodbye")
		break 
	elif ans !="":
		print("\n Not Valid Choice Try again")
GPIO.cleanup()
print "Shutdown All relays"
