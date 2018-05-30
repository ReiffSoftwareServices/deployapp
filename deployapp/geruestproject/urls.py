from django.contrib import admin
from django.conf.urls import  url
from django.urls import path, include
from . import views


## urls on app level. They are redirected to urls on project level.


urlpatterns = [
    path ('home/', views.index, name= 'index'),
    path('accounts/register', views.registration.as_view())   #as_view() for classes
              ]
