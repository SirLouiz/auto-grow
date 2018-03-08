
import time

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

print('Press Ctrl-C to quit...')
while True:
	value1 = mcp.read_adc(0)
	value2 = mcp.read_adc(7)
	print('Humidade: {0}'.format(value1))
	print('Luz: {0}'.format(value2))
	time.sleep(0.5)

