import Adafruit_DHT
import RPi.GPIO as GPIO
import time

sensor = Adafruit_DHT.DHT11

GPIO.setmode(GPIO.BOARD)

pino_sensor = 4

print("Lendo valores de Temperatura e Umidade")

while(1):
	umid, temp = Adafruit_DHT.read_retry(sensor, pino_sensor)
	if umid is not None and temp is not None:
		print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temp, umid))
		time.sleep(5)
	else:
		print("Falha ao ler dados!")
