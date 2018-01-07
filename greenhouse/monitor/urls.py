from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('air_humidity', views.air_humidity, name='air_humidity'),
    path('dirt_humidity', views.dirt_humidity, name='dirt_humidity'),
    path('light', views.light, name='light'),
    path('temp', views.temperature, name='temp'),
]
