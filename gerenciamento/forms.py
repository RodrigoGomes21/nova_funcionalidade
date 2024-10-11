from django import forms
from .models import Time

#Parte das Formas de Time

class TimeForm(forms.ModelForm):
    class Meta:
        model = Time
        fields = ['nome', 'modalidade']
