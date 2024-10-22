from django import forms
from .models import Time

#para cadastro de times 

class TimeForm(forms.ModelForm):
    class Meta:
        model = Time
        fields = ['nome', 'modalidade'] 