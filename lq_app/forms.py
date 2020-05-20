from django import forms
from basic.models import Customer, Laundrer, Load

from django.contrib.auth import get_user_model
User = get_user_model()

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email','password')

class CustomerForm(forms.ModelForm):
    class Meta():
        model = Customer
        fields = ('email','phone_number', 'dorm')


class LaundrerForm(forms.ModelForm):
    class Meta():
        model = Laundrer
        fields = ('email','phone_number', 'dorm')

class LoadForm(forms.ModelForm):
    class Meta():
        model = Load
        fields = ('customer','items_no', 'baskets_no')


