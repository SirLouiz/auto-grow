from django.http import HttpResponse
import paho.mqtt.subscribe as subscribe


def get_data(topic):
    data = subscribe.simple(topic, hostname="201.21.190.179", port=42400, retained=False, msg_count=10)
    res = ""
    for h in data:
        res = res + str(h.payload) + "\n"
    return str(res)


def index(request):
    return HttpResponse("GreenHouse")


def air_humidity(request):
    return HttpResponse(get_data("monitor/air"))


def dirt_humidity(request):
    return HttpResponse(get_data("monitor/dirt"))


def light(request):
    return HttpResponse(get_data("monitor/light"))


def temperature(request):
    return HttpResponse(get_data("monitor/temp"))
