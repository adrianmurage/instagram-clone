from django.shortcuts import render, redirect
from .models import User, Followers
from .forms import *
from django.contrib.auth import authenticate, login, logout as dlogout


def ajaxsignup(request):
    '''
    function that handles the signup process
    '''
    ajax = AjaxSignUp(request.POST)
    context = {'ajax_output': ajax.output()}
    return render(request, 'ajax.html', context)


def ajaxlogin(request):
    '''
    function that handles the login process by running the validation
    '''
    ajax = AjaxLogin(request.POST)
    logged_in_user, output = ajax.validate()
    if logged_in_user is not None:
        login(request, logged_in_user)
    context = {'ajax_output': output}
    return render(request, 'ajax.html', context)


def ajaxsavephoto(request):
    '''
    function to save uploaded photo urls and details to the database
    '''
    ajax = AjaxSavePhoto(request.POST, request.user)
    context = {'ajax_output': ajax.output()}
    return render(request, 'ajax.html', context)


def ajaxphotofeed(request):
    '''
    function to process the photo feed for our app
    '''
    ajax = AjaxPhotoFeed(request.GET, request.user)
    context = {'ajax_output': ajax.output()}
    return render(request, 'ajax.html', context)


def ajaxprofilefeed(request):
    '''
    function to process the users profile feed
    '''
    ajax = AjaxProfileFeed(request.GET, request.user)
    context = {'ajax_output': ajax.output()}
    return render(request, 'ajax.html', context)


def ajaxsetprofilepic(request):
    ajax = AjaxSetProfilePic(request.POST, request.user)
    context = {'ajax_output': ajax.output()}
    return render(request, 'ajax.html', context)


def ajaxlikephoto(request):
    ajax = AjaxLikePhoto(request.GET, request.user)
    context = {'ajax_output': ajax.output()}
    return render(request, 'ajax.html', context)


def ajaxfollow(request):
    ajax = AjaxFollow(request.GET, request.user)
    context = {'ajax_output': ajax.output()}
    return render(request, 'ajax.html', context)


def signup(request):
    '''
    function to render sign-up.html and handle user signup
    '''
    context = {}
    return render(request, 'auth/sign-up.html', context)


def logout(request):
    context = {}
    dlogout(request)
    return redirect(home)


def home(request):
    '''
    function to render index.html and handle user signin
    '''
    context = {}
    if request.user.is_authenticated:
        u = User.objects.filter(username=request.user.username)[0]
        if u.profilepic == "":
            u.profilepic = "static/images/default.png"
        context = {'user': request.user, 'ProfilePic': u.profilepic}
        return render(request, 'loggedin/logged-in-index.html', context)

    return render(request, 'auth/index.html', context)


def profile(request, username):
    '''
    function to render the profile page
    '''
    if User.objects.filter(username=username).exists():
        u = User.objects.filter(username=username)[0]

        if not Followers.objects.filter(user=username, follower=request.user.username).exists():
            following = "Follow"
        else:
            following = "Unfollow"

        if u.profilepic == "":
            u.profilepic = "static/images/default.png"
        context = {"ProfilePic": u.profilepic, "whosprofile": username, "logged_in_as": request.user.username, "following": following}
        if request.user.is_authenticated:
            return render(request, 'loggedin/logged-in-profile.html', context)
        return render(request, 'profile.html', context)
    else:
        return redirect(home)
