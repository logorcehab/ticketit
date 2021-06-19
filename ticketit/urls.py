"""ticketit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from user.urls import urlpatterns as user_urls
from django.contrib.auth import views as auth
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    #Users 
    path('', include(user_urls)),


    #Event
    path('', views.home, name="home"),
    path('movies/', views.movies, name="movies"),
    path('buy-ticket/<int:item_id>/', views.BuyTicket, name="buy-ticket"),
    path('buy-confirm/<int:item_id>/<int:count>/', views.BuyConfirm, name="buy-confirm"),
]
