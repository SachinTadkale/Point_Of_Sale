from django.shortcuts import render, redirect
from django.contrib import messages
from products.models import Product

# Create your views here.

def sales(request):
    messages.info(request, 'Sales functionality is temporarily disabled.')
    return redirect('core:home')
