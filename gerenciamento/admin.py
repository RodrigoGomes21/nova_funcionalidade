from django.contrib import admin
from .models import Bolsista, Participante, Frequencia,Time
#adiciodas novas bibliotecas 22/10/24
from django.http import HttpResponseRedirect
from django.utils.html import format_html
from django.urls import path

class FrequenciaAdmin(admin.ModelAdmin):
    list_display = ('bolsista', 'mes', 'frequencia_entregue', 'frequencia_participantes_entregue')
    list_filter = ('mes', 'bolsista',)
    search_fields = ['bolsista__nome']
    list_editable = ('frequencia_entregue', 'frequencia_participantes_entregue')
    
    

#parte do cadastro de times 22/10/24
class TimeAdmin(admin.ModelAdmin):
    def cadastrar_time_link(self):
        # Adiciona um link para "Cadastrar Time"
        return format_html('<a href="/admin/time/cadastrar_time/">Cadastrar Time</a>')

    cadastrar_time_link.short_description = 'Cadastrar Time'

    def get_urls(self):
        # Adiciona uma URL customizada ao admin
        urls = super().get_urls()
        custom_urls = [
            path('cadastrar_time/', self.admin_site.admin_view(self.cadastrar_time_view))
        ]
        return custom_urls + urls

    def cadastrar_time_view(self, request):
        # Redireciona para a página de cadastro de times
        return HttpResponseRedirect('/admin/time/cadastrar_time/')

# Registrar o modelo Time com o TimeAdmin personalizado
admin.site.register(Time, TimeAdmin)




class ParticipanteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'modalidade', 'curso')  # Adiciona as colunas visíveis na listagem
    list_filter = ('modalidade', 'curso', 'competidor')  # Adiciona filtros por modalidade e curso
 

admin.site.register(Bolsista)
admin.site.register(Participante, ParticipanteAdmin)  # Certifique-se de registrar o admin com o ParticipanteAdmin
admin.site.register(Frequencia, FrequenciaAdmin)


#É ESSA PAGINA ONDE EU CONSIGO GERENCIAR OS FILTROS DE PESQUISA



