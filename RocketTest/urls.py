"""RocketTest URL Configuration

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
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from rest_framework import routers

from RocketTestApp import views
router = routers.DefaultRouter()
router.register(r'user', views.UserAppQuerySet, basename="")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/singup', views.createUser, name='create_user'),
    path('', include(router.urls)),
    #1 - 4 exercises
    path('closer-prime/<int:number>', views.closePrime, name='closer_prime'),
    path('pokemon-type/<str:name>', views.getPokemonType, name='get_pokemon_type'),
    path('pokemon-type-array/<str:name>', views.getPokemonTypeArray, name='get_pokemon_type_array'),
    path('pokemon-type-array-started/<str:name>/<str:start>', views.getPokemonTypeArrayStartWith, name='get_pokemon_type_array_started'),
]
