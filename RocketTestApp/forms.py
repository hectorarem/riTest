from django import forms
from RocketTestApp import models


class SignUpForm(forms.ModelForm):
    class Meta:
        model = models.UserApp
        fields = [
            'email',
            'password',
        ]
    def clean(self):
        email = str(self.cleaned_data.get('email'))
        username = email.split('@')[0] + '_' +email.split('@')[1].split('.')[0]
        self.cleaned_data.setdefault('username',  username )
        self.cleaned_data.setdefault('email', email)

class UserUpdate(forms.ModelForm):
    class Meta:
        model = models.UserApp
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'phonePrefix',
            'phone',
        ]