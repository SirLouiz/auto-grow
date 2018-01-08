import time
import paho.mqtt.subscribe as subscribe


while True:
        #result = get_data("control/light")
        data = subscribe.simple("control/light", hostname="192.168.1.105", retained=False, msg_count=1)        
	res = ""
        #for h in data:
        res = res + str(data.payload) + "\n"
        print(res)

