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

# Type of sensor, can be Adafruit_DHT.DHT11, Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
DHT_TYPE = Adafruit_DHT.DHT11
# Example of sensor connected to Raspberry Pi pin 23
DHT_PIN  = 4

# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))
print("Preparação Concluida")
while True:
	tempo = strftime(" %H:%M:%S ")
	if tempo =="17:":
		print(tempo)



