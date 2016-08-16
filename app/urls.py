from django.conf.urls import url

from . import views

url(r'^$', views.index, name='index'),