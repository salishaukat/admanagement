from django import forms
from django.contrib.auth.models import User
from .models import Category,Ad


class AdForm(forms.ModelForm):

    class Meta:
        model = Ad
        fields = ['adText', 'adUrl', 'category_id']

