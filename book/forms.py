from django.forms import ModelForm
from django import forms
# from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import *


class AddBookForm(ModelForm):

    class Meta:
        model = Book
        exclude = ['user']
