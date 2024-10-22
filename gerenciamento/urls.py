from django.urls import path
from . import views  # Importa as views do app gerenciamento

urlpatterns = [
    path('', views.index, name='index'),  # Define a rota para a função 'index'
    path('participantes/', views.lista_participantes, name='lista_participantes'),  # Rota para listar participantes
]

urlpatterns = [
    #essa é a rota do cadastro de times
    path('times/cadastrar/', views.cadastrar_time, name='cadastrar_time'),
    path('times/', views.lista_times, name='lista_times'),
]
