'''
setup urls for our instagram app
'''
from django.conf.urls import url
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^sign-up$', views.signup, name='signup'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^(?P<username>[a-zA-Z0-9_.]+)$', views.profile, name='profile'),
    url(r'^ajax-sign-up$', views.ajaxsignup, name='ajaxsignup'),
    url(r'^ajax-login$', views.ajaxlogin, name='ajaxlogin'),
    url(r'^ajax-save-photo$', views.ajaxsavephoto, name='ajaxsavephoto'),
    url(r'^ajax-photo-feed$', views.ajaxphotofeed, name='ajaxphotofeed'),
    url(r'^ajax-profile-feed$', views.ajaxprofilefeed, name='ajaxprofilefeed'),
    url(r'ajax-set-profile-pic$', views.ajaxsetprofilepic, name='ajaxsetprofilepic'),
    url(r'^ajax-like-photo$', views.ajaxlikephoto, name='ajaxlikephoto'),
    url(r'^ajax-follow$', views.ajaxfollow, name='ajaxfollow'),
]
