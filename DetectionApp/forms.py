from django import forms
from .models import Image
from django.forms import ModelForm, TextInput


class ImageForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Enter your name'
        }
    ))
    age = forms.CharField(widget=forms.NumberInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Enter your age'
        }
    ))
    email = forms.CharField(widget=forms.EmailInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Enter your email address'
        }
    ))
    country = forms.CharField(widget=forms.TextInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Enter country of residence'
        }
    ))
    image = forms.ImageField(widget=forms.FileInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Choose image',
        }
    ))

    class Meta:
        model = Image
        fields = ('title', 'age', 'email', 'country', 'image')