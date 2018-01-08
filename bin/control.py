import time
import paho.mqtt.subscribe as subscribe

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

def get_data(topic):
	data = subscribe.simple(topic, retained=False, msg_count=1)
	res = ""
	res = res + str(data.payload)
	return str(res)


while True:
	print("Waiting Command")
	data = get_data("control/light")
	print data
	if data=="1":
                if GPIO.input(13)==1:
                        GPIO.output(13,  GPIO.LOW)
                elif GPIO.input(13)==0:
                        GPIO.output(13,  GPIO.HIGH)
        elif data=="2":
                if GPIO.input(19)==1:
                        GPIO.output(19,  GPIO.LOW)
                elif GPIO.input(19)==0:
                        GPIO.output(19,  GPIO.HIGH)
        elif data=="3":
                if GPIO.input(26)==1:
                        GPIO.output(26,  GPIO.LOW)
                elif GPIO.input(26)==0:
                        GPIO.output(26,  GPIO.HIGH)
	elif data=="4":
		print("Goodbye")
		GPIO.output(pins, GPIO.HIGH)
		continue
GPIO.cleanup()
print "Shutdown All relays"



