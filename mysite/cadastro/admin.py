from django.contrib import admin
from .models import Projeto, Deputado, Tramitacao, TipoReuniao, Comissao, ControleReuniao

# Register your models here.



class ProjetoAdmin(admin.ModelAdmin):
    pass


class DeputadoAdmin(admin.ModelAdmin):
    pass


class TramitacaoAdmin(admin.ModelAdmin):
    pass


class TipoReuniaoAdmin(admin.ModelAdmin):
    pass


class ComissaoAdmin(admin.ModelAdmin):
    pass


class ControleReuniaoAdmin(admin.ModelAdmin):
    pass


admin.site.register(TipoReuniao, TipoReuniaoAdmin)
admin.site.register(Comissao, ComissaoAdmin)
admin.site.register(Deputado, DeputadoAdmin)
admin.site.register(Projeto, ProjetoAdmin)
admin.site.register(ControleReuniao, ControleReuniaoAdmin)
admin.site.register(Tramitacao, TramitacaoAdmin)

