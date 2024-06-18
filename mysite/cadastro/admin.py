from django.contrib import admin

# Register your models here.

from .models import Projeto, Deputado, Tramitacao, TipoReuniao, Comissao, ControleReuniao

admin.site.register(TipoReuniao)
admin.site.register(Comissao)
admin.site.register(Deputado)
admin.site.register(Projeto)
admin.site.register(ControleReuniao)
admin.site.register(Tramitacao)
