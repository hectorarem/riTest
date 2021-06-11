from django.http import JsonResponse
import requests

from RocketTest.settings import POKEMON_API
from RocketTestApp import models, forms, utils


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

def updateUser(request, pk):
    if request.POST:
        form = forms.UserUpdate(request.POST)
        if form.is_valid():
            if request.user.is_superuser or request.user.pk == pk:
                user = models.UserApp.objects.get(pk=pk)
                user.username = form.cleaned_data.get('username')
                user.email = form.cleaned_data.get('email')
                user.first_name = form.cleaned_data.get('first_name')
                user.last_name = form.cleaned_data.get('last_name')
                user.phonePrefix = form.cleaned_data.get('phonePrefix')
                user.phone = form.cleaned_data.get('phone')
                user.save()
                return JsonResponse({'success': 'User updated successfully'})
            else:
                return JsonResponse({'error': 'Are you hacking us??. NO HERE!!'})
        else:
            return JsonResponse({'error': 'Something is wrong in your form, check again!'})
    else:
        return JsonResponse({'error': 'Must be a POST request'})

def getUser(request, pk):
    try:
        res = {}
        user = models.UserApp.objects.get(pk=pk)
        res['uui'] = user.uui
        res['username'] = user.username
        res['first_name'] = user.first_name
        res['last_name'] = user.last_name
        res['email'] = user.email
        res['is_active'] = user.is_active
        res['phonePrefix'] = user.phonePrefix
        res['phone'] = user.phone
        res['last_login'] = user.last_login
        res['date_joined'] = user.date_joined
        res['is_staff'] = user.is_staff
        return JsonResponse(res)
    except:
        return JsonResponse({'error': 'The user do not exist in our database'})

def userDelete(request, pk):
    if request.user.is_superuser:
        try:
            models.UserApp.objects.get(pk=pk).delete()
            return JsonResponse({'success': 'User deleted'})
        except:
            return JsonResponse({'error': 'Ups!, user dont found'})
    elif request.user.pk == pk:
        user = models.UserApp.objects.get(pk=pk)
        user.is_active = False
        user.save()
        return JsonResponse({'success': 'You delete your account successfully'})
    else:
        return JsonResponse({'error': 'Are you hacking us??. NO HERE!!'})

