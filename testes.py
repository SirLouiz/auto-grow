import time

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import Adafruit_DHT

# Type of sensor, can be Adafruit_DHT.DHT11, Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
DHT_TYPE = Adafruit_DHT.DHT11
# Example of sensor connected to Raspberry Pi pin 23
DHT_PIN  = 4

# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

print('Press Ctrl-C to quit...')
while True:
	humidity, temp = Adafruit_DHT.read(DHT_TYPE, DHT_PIN)
	if humidity is None or temp is None:
        	time.sleep(1)
        	continue
	value1 = mcp.read_adc(0)
	value2 = mcp.read_adc(7)
	print('Humidade: {0}'.format(value1))
	print('Luz: {0}'.format(value2))
	print('Temperatura: {0:0.1f} C'.format(temp))
	print('Humidade do AR:    {0:0.1f} %'.format(humidity))
	time.sleep(2.5)

