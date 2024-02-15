import django.forms
from django import forms
from . import models
from ShaRoSa.models import *
class Sharosasignup(django.forms.Form):    
    mail=django.forms.EmailField()
    password=django.forms.CharField(widget=django.forms.PasswordInput())
    confrmpasswrd=django.forms.CharField(widget=django.forms.PasswordInput())
class SharosaLoginForm(django.forms.Form):
    mail=django.forms.EmailField()
    password=django.forms.CharField(widget=django.forms.PasswordInput())