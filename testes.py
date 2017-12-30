import time
# Import SPI library (for hardware SPI), MCP3008 library and DHT library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import Adafruit_DHT

# Type of sensor, can be Adafruit_DHT.DHT11, Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
DHT_TYPE = Adafruit_DHT.DHT11
# Pin in the RaspberryPi you want to connect the sensor to.
DHT_PIN  = 4

# Hardware SPI configuration for MCP comunication:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

print('Press Ctrl-C to quit...')
# Never ending loop
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

