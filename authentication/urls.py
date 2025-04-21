from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'authentication'

urlpatterns = [
  path('signup/',views.signup,name='signup'),
  path('login/',views.login_view,name='login'),
  path('logout/', views.logout, name='logout'),
  path('users/', views.user_list, name='user_list'),
  path('users/create/', views.user_create, name='user_create'),
  path('users/<int:pk>/edit/', views.user_edit, name='user_edit'),
  path('users/<int:pk>/delete/', views.user_delete, name='user_delete'),
]