from django.shortcuts import render, redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse
import pandas as pd
from .rf import prediction, preprocess
from sklearn.preprocessing import LabelEncoder


# Create your views here.


def index(request):
    if request.user.is_anonymous:
        return redirect("/signup")
    # return HttpResponse("this is homepage")
    return render(request, "index.html")


def signupUser(request):

    if request.method == "POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(
            request, "Your Account has been successfully created!!")

    return render(request, "signup.html")


def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # check if user has enterd correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            fname = user.get_username
            return render(request, "index.html", {'fname': fname})

        else:
            messages.error(request, "Bad Credentials!!!")
            return redirect("/")

    return render(request, "login.html")


def logoutUser(request):
    logout(request)
    messages.success(request, "Log out successfully!!")

    return redirect("/login")


def tweetModel(request):

    return render(request, "tweetModel.html")


def formInfo(request):
    if request.user.is_anonymous:
        return redirect("/signup")

    if request.method == 'POST':

        #insert the tweet into Tweet
        Tweet = request.POST.get('tweet')
        # make a data frame into tweet 
        data_frame = pd.DataFrame({
            'tweet': Tweet,
        }, index=[0])
        
        
        

        processed_data = preprocess(Tweet)

        result = prediction(processed_data)

        print(result)

        if result == 0:
            result = 'you are not racist/sexist '
        else:
            result = 'you are racist/sexist'

        print(result)

    return render(request, 'result.html', {'result': result})

