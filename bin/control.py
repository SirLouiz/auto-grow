import time
import RPi.GPIO as GPIO
import paho.mqtt.subscribe as subscribe

def get_data(topic):
	data = subscribe.simple(topic, hostname="192.168.1.127", retained=False, msg_count=1)
	res = ""
	for h in data:
		res = res + str(h.payload) + "\n"
	return str(res)



while True:
	result = get_data("control/light")
        res = res + str(data.payload) + "\n"
	print(res)

