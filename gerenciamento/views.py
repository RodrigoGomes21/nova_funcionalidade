from django.http import HttpResponse
from django.shortcuts import render
from .models import Participante
from .forms import TimeForm
from django.shortcuts import render, redirect

def index(request):
    return HttpResponse("Hello, this is the index page of gerenciamento.")


# Nova view para listar participantes
def lista_participantes(request):
    modalidade_selecionada = request.GET.get('modalidade')  # Obtém a modalidade selecionada no front-end
    if modalidade_selecionada:
        participantes = Participante.objects.filter(modalidade=modalidade_selecionada)
    else:
        participantes = Participante.objects.all()
    
    modalidades = Participante.objects.values_list('modalidade', flat=True).distinct()  # Lista de modalidades para o filtro
    
    return render(request, 'participantes.html', {
        'participantes': participantes,
        'modalidades': modalidades,
        'modalidade_selecionada': modalidade_selecionada,
    })


def frequencias_view(request):
    return render(request, 'gerenciamento/dj_frequencias.html')

#Parte Do Cadastro dos Times

def cadastrar_time(request):
    if request.method == 'POST':
        form = TimeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_times')
    else:
        form = TimeForm()
    
    return render(request, 'usuarios/cadastrar_time.html', {'form': form})
