  GNU nano 2.7.4                                                                                 Arquivo: teste.py                                                                                              

import time
from time import gmtime, strftime
import RPi.GPIO as GPIO

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import Adafruit_DHT

#Aqui começa a config do Relê
# setting a current mode
GPIO.setmode(GPIO.BCM)
#removing the warings
GPIO.setwarnings(False)
#creating a list (array) with the number of GPIO's that we use 13 e 19 são as duas lampadas e 26 a bomba d'agua
pins = [13,19,26]
#setting the mode as Output, and initial state as HIGH bcuz lamps turn OFF with HIGH and turn ON with LOW
GPIO.setup(pins, GPIO.OUT, initial=GPIO.HIGH)
#Aqui termina a config do Relê

#Aqui começa a config do DHT11
# Type of sensor, can be Adafruit_DHT.DHT11, Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
DHT_TYPE = Adafruit_DHT.DHT11
# Example of sensor connected to Raspberry Pi pin 23
DHT_PIN  = 4

#Aqui começa a config do MCP3008
# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

f = open('out.txt', 'a')
print('Press Ctrl-C to quit...')

for pin in pins:
        #setting the GPIO to HIGH or 1 or true
        GPIO.output(pin,  GPIO.HIGH)
        #wait 0,5 second
        time.sleep(0.5)
        #setting the GPIO to LOW or 0 or false
        GPIO.output(pin,  GPIO.LOW)
        #wait 0,5 second
        time.sleep(0.5)
#limpa todos os sinais dos pinos
GPIO.cleanup()
print "Shutdown All relays"

while True:
	# Reads the DHT Sensor
	humidity, temp = Adafruit_DHT.read(DHT_TYPE, DHT_PIN)
	# If the reading wasn't successful, it waits and reads again
	if humidity is None or temp is None:
        	time.sleep(1) # Waits 1 second
        	continue # Goes back to the begining of the loop
	# Reads the MCP analog inputs given by the Sensors connected to pins 0 and 7 of MCP.
	value1 = mcp.read_adc(0) # Soil Humidity sensor
	value2 = mcp.read_adc(7) # Light sensor
	# Prints all the values collected
	print('Humidade do Solo: {0}'.format(value1))
	print('Luz: {0}'.format(value2))
	print('Temperatura: {0:0.1f} C'.format(temp))
	print('Humidade do Ar:    {0:0.1f} %'.format(humidity))
	time.sleep(2.5)

