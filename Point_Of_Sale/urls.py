"""
URL configuration for Point_Of_Sale project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from authentication import views as auth_views_custom

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='home/', permanent=False)),
    path('home/', include('core.urls')),
    path('products/', include('products.urls')),
    # path('sales/', include('sales.urls')),  # Temporarily commented out
    # path('reports/', include('reports.urls')),  # Temporarily commented out
    path('auth/', include('authentication.urls', namespace='authentication')),
    path('accounts/login/', RedirectView.as_view(url='/auth/login/', permanent=False)),
    path('login/', RedirectView.as_view(url='/auth/login/', permanent=False)),
]
