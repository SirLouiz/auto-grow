import time
from time import gmtime, strftime
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import Adafruit_DHT

import paho.mqtt.client as mqtt

mqttc = mqtt.Client(client_id="monitor", transport="websockets")
mqttc.connect("localhost", 1883, 60)

def on_publish(client, data, mid):
    print("mid: " + str(mid))
pass

mqttc.on_publish = on_publish

# Type of sensor, can be Adafruit_DHT.DHT11, Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
DHT_TYPE = Adafruit_DHT.DHT11
# Example of sensor connected to Raspberry Pi pin 23
DHT_PIN  = 4

# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))
print("Iniciando monitor...")
while True:
	humi, temp = Adafruit_DHT.read(DHT_TYPE, DHT_PIN)
	if humi is None or temp is None:
	       	time.sleep(0.2)
	       	continue
	tempo = strftime(" %H:%M:%S ")
	value1 = mcp.read_adc(0)
	value2 = mcp.read_adc(7)
	#print('Luz: {0}'.format(str(value2)+tempo))
	mqttc.publish("monitor/light",value2)
	mqttc.publish("monitor/air", payload=humi)
	mqttc.publish("monitor/dirt",value1)
	mqttc.publish("monitor/temp",temp)
	mqttc.publish("monitor/time",tempo)
