from django import forms
from django.http import request
from django.shortcuts import redirect


class ContactForm(forms.Form):
    message = forms.CharField(max_length=255)
    subject = forms.CharField(max_length=65536)
    sender = forms.EmailField()

