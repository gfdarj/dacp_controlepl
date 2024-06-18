from django.urls import path

from . import views
from .views import TemplateView, ComissaoListView, ComissaoUpdateView, ComissaoCreateView, ComissaoDeleteView, \
            DeputadoListView, DeputadoCreateView, DeputadoUpdateView, DeputadoDeleteView, \
            TipoReuniaoListView, TipoReuniaoCreateView, TipoReuniaoDeleteView, TipoReuniaoUpdateView, \
            ProjetoListView, ProjetoCreateView, ProjetoUpdateView, ProjetoDeleteView, \
            TramitacaoListView, TramitacaoDeleteView, \
            ControleReunioesListView, ControleReunioesComissaoListView, ControleReuniaoCreateView

appname = "cadastro_um"

urlpatterns = [
    #path('', views.index, name='index'),
    path('', TemplateView.as_view(template_name="cadastro/index.html"), name='index'),

    # LISTA DE COMISSOES
    #path('comissaolista/', views.comissao_lista, name='comissao_lista'),            # LISTA
    path('comissoes/', ComissaoListView.as_view(), name="lista_comissoes"),         # LISTA
    path('comissaoinsere/', ComissaoCreateView.as_view(), name='comissao_insere'),  # INSERE
    path('comissaoedita/<int:pk>', ComissaoUpdateView.as_view(), name='comissao_edita'),   # EDITA
    path('comissaoexcluir/<int:pk>', ComissaoDeleteView.as_view(), name='comissao_excluir'),  # EXCLUI

    path('deputados/', DeputadoListView.as_view(), name="lista_deputados"),  # LISTA
    path('deputadoinsere/', DeputadoCreateView.as_view(), name='deputado_insere'),  # INSERE
    path('deputadoedita/<int:pk>', DeputadoUpdateView.as_view(), name='deputado_edita'),  # EDITA
    path('deputadoexcluir/<int:pk>', DeputadoDeleteView.as_view(), name='deputado_excluir'),  # EXCLUI

    path('tiposreunioes/', TipoReuniaoListView.as_view(), name="lista_tiposreunioes"),  # LISTA
    path('tiporeuniaoinsere/', TipoReuniaoCreateView.as_view(), name='tiporeuniao_insere'),  # INSERE
    path('tiporeuniaoedita/<int:pk>', TipoReuniaoUpdateView.as_view(), name='tiporeuniao_edita'),  # EDITA
    path('tiporeuniaoexcluir/<int:pk>', TipoReuniaoDeleteView.as_view(), name='tiporeuniao_excluir'),  # EXCLUI

    path('projetos/', ProjetoListView.as_view(), name="lista_projetos"),  # LISTA
    path('projetoinsere/', ProjetoCreateView.as_view(), name='projeto_insere'),  # INSERE
    path('projetoedita/<int:pk>', ProjetoUpdateView.as_view(), name='projeto_edita'),  # EDITA
    path('projetoexcluir/<int:pk>', ProjetoDeleteView.as_view(), name='projeto_excluir'),  # EXCLUI

    path('tramitacoes/<int:pk>', TramitacaoListView.as_view(), name="lista_tramitacoes"),  # LISTA
    path('tramitacaoexcluir/<int:pk>', TramitacaoDeleteView.as_view(), name='tramitacao_excluir'),  # EXCLUI

    path('reunioescomissao/', ControleReunioesComissaoListView.as_view(), name="lista_controlereunioes_comissao"),  # LISTA
    path('controlereunioes/<int:pk>', ControleReunioesListView.as_view(), name="lista_controlereunioes"),  # LISTA
    path('controlereuniaoinsere/<int:pk>', ControleReuniaoCreateView.as_view(), name='controlereuniao_insere'),  # INSERE

    #######

    path('deputadolista/', views.deputado_lista, name='deputado_lista'),
    path('<int:deputado_id>/deputadoedita/', views.deputado_edita, name='deputadoedita'),

    path('comissoes1/<pk>', ComissaoUpdateView.as_view(), name="atualiza_comissao"),  # GET/POST /funcionario/{pk}
]
