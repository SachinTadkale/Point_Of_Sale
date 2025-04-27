from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'core'

urlpatterns = [
  path('dashboard/',views.dashboard,name='dashboard'),
  path('', views.landing, name='home'),
  path('home/', views.home, name='home'),
  path('contact/', views.contact_view, name='contact'),
]