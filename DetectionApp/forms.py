from django import forms
from .models import Image
from django.forms import ModelForm, TextInput


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'image')