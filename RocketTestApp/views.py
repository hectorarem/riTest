from django.http import JsonResponse
import requests
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from RocketTest.settings import POKEMON_API
from RocketTestApp import models, forms, utils
from RocketTestApp.models import UserApp
from RocketTestApp.serializers import UserAppSerializer


def closePrime(request, number):
    res = {
        'number posted': number,
        'number posted is prime too?': 'Yes' if utils.isPrime(number) else 'No',
        'closer prime': utils.closePrimeNumber(number),
    }
    return JsonResponse(res)

def getPokemonType(request, name):
    url = f"{POKEMON_API}type/{name}"
    response = requests.get(url)
    if response.ok:
        return JsonResponse(response.json())
    else:
        return JsonResponse({'error': response.status_code})

def getPokemonTypeArray(request, name):
    url = f"{POKEMON_API}type/{name}"
    response = requests.get(url)
    if response.ok:
        try:
            pokemons = response.json()['pokemon']
            return JsonResponse({'count': len(pokemons), 'pokemons': pokemons})
        except:
            return JsonResponse({})
    else:
        return JsonResponse({'error': response.status_code})

def getPokemonTypeArrayStartWith(request, name, start):
    url = f"{POKEMON_API}type/{name}"
    response = requests.get(url)
    if response.ok:
        try:
            pokemons = response.json()['pokemon']
            filter = [value for value in pokemons if (str(value['pokemon']['name'][0:len(start)]).lower() == start)]
            res = {
                'start with': start,
                'count': len(filter),
                'pokemons': filter
            }
            return JsonResponse(res)
        except:
            return JsonResponse({})
    else:
        return JsonResponse({'error': response.status_code})

def createUser(request):
    if request.POST:
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            try:
                models.UserApp.objects.create_user(username=username, email=email, password=password)
                return JsonResponse({'success': 'User created successfully'})
            except:
                return JsonResponse({'error': 'The user exist in our database, restore your password!'})
        else:
            return JsonResponse({'error': 'Something is wrong in your form, check again!'})
    else:
        return JsonResponse({'error': 'Must be a POST request'})

class UserAppQuerySet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserAppSerializer
    http_method_names = ['get', 'put', 'patch', 'delete']
    lookup_field = 'uui' #filtrar por el uuid del userApp

    def get_queryset(self):
        if self.request.user.is_staff or self.request.user.is_superuser:
            return UserApp.objects.order_by('-pk')
        else:
            return UserApp.objects.filter(pk=self.request.user.pk)

    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        user.is_active = False
        user.save()
        return JsonResponse({'success': 'user deleted successfully'})
