from django.contrib import admin
from .models import *

admin.site.register(Cidade)
admin.site.register(Ocupacao)
admin.site.register(Pessoa)
admin.site.register(Instituicao)
admin.site.register(Veiculo)
admin.site.register(Rota)
admin.site.register(Frequencia)
admin.site.register(Horario)
admin.site.register(Ocorrencia)
admin.site.register(Gasto)
admin.site.register(Tipo)

# @admin.register(Chat)
# class ChatAdmin(admin.ModelAdmin):
#     list_display = ('id', 'pessoa', 'criado_em')
#     list_filter = ('criado_em',)
#     search_fields = ('mensagem', 'pessoa__nome')