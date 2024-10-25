# forms.py

from django import forms
from .models import Time, Participante

class TimeForm(forms.ModelForm):
    # Campo para adicionar participantes
    participante_nome = forms.CharField(max_length=100, required=False, label='Adicionar Participante')

    class Meta:
        model = Time
        fields = ['nome', 'modalidade']  # Campos já existentes
    
    def clean_participante_nome(self):
        # Lógica de validação para o limite de participantes
        participante_nome = self.cleaned_data.get('participante_nome')
        modalidade = self.cleaned_data.get('modalidade')
        if modalidade:
            max_participantes = {
                'basquete': 12,
                'futsal': 14,
                'handebol': 14,
                'volei': 10
            }
            limite = max_participantes.get(modalidade)
            participantes_atuais = Participante.objects.filter(modalidade=modalidade).count()
            if participantes_atuais >= limite:
                raise forms.ValidationError(f'O limite para {modalidade} é de {limite} participantes.')
        return participante_nome
