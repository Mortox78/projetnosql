"""projetnosql URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from .views import add_book, book_list, index, dogs_list, dogs_search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('add_book/', add_book, name='add_book'),
    path('book_list/', book_list, name='book_list'),
    path('dogs/search', dogs_search, name='dogs_search'),
    path('dogs_list/', dogs_list, name='dogs_list'),
]