from django.shortcuts import render, redirect
from .models import User
from .forms import *


def signup(request):
    '''
    function to render sign-up.html and handle user signup
    '''
    context = {}
    return render(request, 'sign-up.html', context)


def index(request):
    '''
    function to render index.html and handle user signin
    '''
    context = {}
    return render(request, 'index.html', context)
