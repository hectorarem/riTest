from django.http import JsonResponse

from RocketTestApp import models, forms


def createUser(request):
    if request.POST:
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            print(form.cleaned_data)
            password = form.cleaned_data.get('password')
            print(username, email, password)
            models.UserApp.objects.create_user(username=username, email=email, password=password)
            return JsonResponse({'success': 'User created successfully'})
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
        delete = models.UserApp.objects.get(pk=pk).delete()
        if delete:
            return JsonResponse({'success': 'User deleted'})
        else:
            return JsonResponse({'error': 'Ups!, user was not deleted'})
    elif request.user.pk == pk:
        user = models.UserApp.objects.get(pk=pk)
        user.is_active = False
        user.save()
        return JsonResponse({'success': 'You delete your account successfully'})
    else:
        return JsonResponse({'error': 'Are you hacking us??. NO HERE!!'})

