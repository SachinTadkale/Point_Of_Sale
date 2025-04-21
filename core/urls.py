from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'core'

urlpatterns = [
  path('dashboard/',views.dashboard,name='dashboard'),
  path('', views.home, name='home'),
  path('landing/',views.landing,name='landing'),
]