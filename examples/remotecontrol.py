import time
from time import gmtime, strftime
import paho.mqtt.publish as publish

ans=True
aux1=0
while ans:
        print ("""
        1.Liga/Desl luz 1
        2.Liga/Desl luz 2
        3.Liga/Desl bomba
        4.Exit/Quit
        """)
        ans=raw_input("What would you like to do? ")
        if ans=="1":
		publish.single("control/light","1",hostname="192.168.1.120")
        elif ans=="2":
		publish.single("control/light","2",hostname="192.168.1.120")
        elif ans=="3":
		publish.single("control/light","3",hostname="192.168.1.120")
        elif ans=="4":
		publish.single("control/light","4",hostname="192.168.1.120")
                print("\n Goodbye")
                break
        elif ans !="":
                print("\n Not Valid Choice Try again")
