from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
  path('about/',views.about,name='about'),
  path('contact/',views.contact,name='contact'),
  path('dashboard/',views.dashboard,name='dashboard'),
  path('home/',views.home,name='home'),
  path('landing/',views.landing,name='landing'),
    
]