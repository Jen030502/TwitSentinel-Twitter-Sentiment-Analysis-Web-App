from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
    path("", views.index, name='home'),
    path("signup", views.signupUser, name='signup'),
    path("login", views.loginUser, name='login'),
    path("logout", views.logoutUser, name='logout'),
    path("tweetModel", views.tweetModel, name='tweetModel'),
    path('result',views.formInfo,name='result')
]
 