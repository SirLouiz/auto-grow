import time
from time import gmtime, strftime

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
bomb = 26
#setting the mode for all pins so all will be switched on
GPIO.setup(lights, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(bomb, GPIO.OUT, initial=GPIO.HIGH)

# Type of sensor, can be Adafruit_DHT.DHT11, Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
DHT_TYPE = Adafruit_DHT.DHT11
# Example of sensor connected to Raspberry Pi pin 23
DHT_PIN  = 4

# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))
print("Preparacao Concluida")
while True:
        soil = mcp.read_adc(0)
        if soil >= "1000": #if soil is dry
                GPIO.output(bomb,  GPIO.LOW)
                continue
        elif soil <= "600": #if soil is wet
                GPIO.output(bomb,  GPIO.HIGH)
	tempo = strftime("%H:%M:%S")
	tempo = tempo.split(":")
	if tempo[0] =="18": #if it is 18oclock and the lights are on
		if GPIO.input(lights)==0:
			GPIO.output(lights,  GPIO.HIGH) #turn off
	elif tempo[0] =="06": #if it is 06oclock and the lights are off
		if GPIO.input(lights)==1:
			GPIO.output(lights,  GPIO.LOW) #turn on
	time.sleep(2000) #wait 30min and read again
