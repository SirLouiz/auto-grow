import time
from time import gmtime, strftime
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import Adafruit_DHT

import paho.mqtt.publish as publish

def on_publish(mqttc, obj, mid):
    print("mid: " + str(mid))
pass

# Type of sensor, can be Adafruit_DHT.DHT11, Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
DHT_TYPE = Adafruit_DHT.DHT11
# Example of sensor connected to Raspberry Pi pin 23
DHT_PIN  = 4

# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

while True:
	humi, temp = Adafruit_DHT.read(DHT_TYPE, DHT_PIN)
	if humi is None or temp is None:
	       	time.sleep(1)
	       	continue
	tempo = strftime(" %H:%M:%S ")
	value1 = mcp.read_adc(0)
	value2 = mcp.read_adc(7)
	print('Luz: {0}'.format(str(value2)+tempo))
	publish.single("monitor/light",tempo+str(value2))
	publish.single("monitor/air",humi)
	publish.single("monitor/dirty",value1)
	publish.single("monitor/temp",temp)
