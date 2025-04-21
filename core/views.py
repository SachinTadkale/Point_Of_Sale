from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def about(request):
  return render(request,'core/about.html')

def contact(request):
  return render(request,'core/contact.html')

def dashboard(request):
  return render(request,'core/dashboard.html')

def home(request):
  return render(request,'core/home.html')

def landing(request):
  return render(request,'core/landing.html')