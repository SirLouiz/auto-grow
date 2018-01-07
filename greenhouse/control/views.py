from django.http import HttpResponse
import paho.mqtt.publish as publish


def send_data(topic, message):
    publish.single(topic, message)


def light_on(request):
    send_data("control/light", "on")
    return HttpResponse("OK")


def light_off(request):
    send_data("control/light", "off")
    return HttpResponse("OK")
