import time
import paho.mqtt.subscribe as subscribe

def get_data(topic):
	data = subscribe.simple(topic,hostname="192.168.1.120",retained=False, msg_count=1)
	res = ""
	#for a in data:
	res = res + str(data.payload) +" "
	return str(res)

while True:
	luz = get_data("monitor/light")
	temp = get_data("monitor/temp")
	air = get_data("monitor/air")
	dirt = get_data("monitor/dirt")
	horas = get_data("monitor/time")
	#luz = luz.split()
	print("------Ultimos Valores Lidos:------")
	print("------Horas: {0}------".format(horas))
	print("------Nivel de Luz: {0}------".format(luz))
	print("------Temperatura: {0}C------".format(temp))
	print("------Humidade do ar: {0}%------".format(air))
	print("------Humidade da Terra: {0}------".format(dirt))
	print ("\n") 
