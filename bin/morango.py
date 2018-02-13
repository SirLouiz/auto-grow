import time
from time import gmtime, strftime

import os
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
lights = [13,19]
pump = 26
#setting the mode for all pins so all will be switched on
GPIO.setup(lights, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(pump, GPIO.OUT, initial=GPIO.HIGH)

# Type of sensor, can be Adafruit_DHT.DHT11, Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
DHT_TYPE = Adafruit_DHT.DHT11
# Example of sensor connected to Raspberry Pi pin 23
DHT_PIN  = 4

# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))
#print("Preparacao Concluida")
while True:
        tempo = strftime("%H:%M:%S")
        if tempo == "23:59:00":
		#print ("Rebooting")
		os.system('systemctl reboot')
		time.sleep(5)
        elif tempo == "06:30:00": #waters once a day for 3s
                GPIO.output(pump, GPIO.LOW) #turn on pump
                time.sleep(5) #waits 3s
		GPIO.output(pump, GPIO.HIGH) #turn off pump
		#time.sleep()
        tempo = tempo.split(":")
	if tempo[0]=="17" and tempo[1]=="59" and GPIO.input(13)==0: #if its 18h and lights on
			GPIO.output(lights,  GPIO.HIGH) #turn off
	elif tempo[0]=="05" and tempo[1]=="59" and GPIO.input(13)==1: #if its 06h and lights off
			GPIO.output(lights,  GPIO.LOW) #turn on
        #soil = mcp.read_adc(0)
