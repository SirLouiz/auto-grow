from django.urls import path

from . import views

urlpatterns = [
    path('light_on', views.light_on, name='light_on'),
    path('light_off', views.light_off, name='light_off'),
]
