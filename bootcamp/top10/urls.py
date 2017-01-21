# coding: utf-8


from django.conf.urls import url
from bootcamp.top10 import views

urlpatterns = [
    url(r'^$', views.DisplayTop10,name='DisplayTop10'),
]
