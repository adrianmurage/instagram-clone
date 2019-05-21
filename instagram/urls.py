'''
setup urls for our instagram app
'''
from django.conf.urls import url
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup$', views.signup, name='signup')
]
