from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, TemplateView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import ComissaoForm, DeputadoForm, TipoReuniaoForm, ProjetoForm, ControleReuniaoForm
from .models import Comissao, Deputado, TipoReuniao, Projeto, Tramitacao, ControleReuniao

# Create your views here.


class ControleReuniaoCreateView(CreateView):
    template_name = "cadastro/controlereuniao_insere.html"
    model = ControleReuniao
    context_object_name = 'projeto'
    form_class = ControleReuniaoForm
    success_url = reverse_lazy("lista_controlereunioes")

    def get_queryset(self):
        return ControleReuniao.objects.filter(comissao_id=self.kwargs['pk'])


class ControleReunioesListView(ListView):
    template_name = "cadastro/controlereuniao_listagem.html"
    model = ControleReuniao
    context_object_name = "controlereunioes"
    # paginate_by = 10

    def get_queryset(self):
        return ControleReuniao.objects.filter(comissao_id=self.kwargs['pk'])


class ControleReunioesComissaoListView(ListView):
    template_name = "cadastro/comissao_listagem_controlereuniao.html"
    model = Comissao
    context_object_name = "comissoes"

    def get_queryset(self):
        return Comissao.objects.filter(ativo=True)

###########################

class TramitacaoListView(ListView):
    template_name = "cadastro/tramitacao_listagem.html"
    model = Tramitacao
    context_object_name = "tramitacoes"

    def get_queryset(self):
        return Tramitacao.objects.filter(projeto_id=self.kwargs['pk'])


class TramitacaoDeleteView(DeleteView):
    template_name = "cadastro/tramitacao_excluir.html"
    model = Tramitacao
    fields = '__all__'
    context_object_name = 'tramitacao'
    success_url = reverse_lazy("lista_tramitacoes")

###########################

class ProjetoListView(ListView):
    template_name = "cadastro/projeto_listagem.html"
    model = Projeto
    #ordering = ['descricao']
    context_object_name = "projetos"


class ProjetoCreateView(CreateView):
    template_name = "cadastro/projeto_insere.html"
    model = Projeto
    #fields = '__all__'
    context_object_name = 'projeto'
    form_class = ProjetoForm
    success_url = reverse_lazy("lista_projetos")


class ProjetoUpdateView(UpdateView):
    template_name = "cadastro/projeto_edita.html"
    model = Projeto
    #fields = '__all__'
    context_object_name = 'projeto'
    form_class = ProjetoForm
    success_url = reverse_lazy("lista_projetos")


class ProjetoDeleteView(DeleteView):
    template_name = "cadastro/projeto_excluir.html"
    model = Projeto
    fields = '__all__'
    context_object_name = 'projeto'
    success_url = reverse_lazy("lista_projetos")

###########################################################################################################

class TipoReuniaoListView(ListView):
    template_name = "cadastro/tiporeuniao_listagem.html"
    model = TipoReuniao
    #ordering = ['descricao']
    context_object_name = "tiposreunioes"


class TipoReuniaoCreateView(CreateView):
    template_name = "cadastro/tiporeuniao_insere.html"
    model = TipoReuniao
    #fields = '__all__'
    context_object_name = 'tiporeuniao'
    form_class = TipoReuniaoForm
    success_url = reverse_lazy("lista_tiposreunioes")


class TipoReuniaoUpdateView(UpdateView):
    template_name = "cadastro/tiporeuniao_edita.html"
    model = TipoReuniao
    #fields = '__all__'
    context_object_name = 'tiporeuniao'
    form_class = TipoReuniaoForm
    success_url = reverse_lazy("lista_tiposreunioes")


class TipoReuniaoDeleteView(DeleteView):
    template_name = "cadastro/tiporeuniao_excluir.html"
    model = TipoReuniao
    fields = '__all__'
    context_object_name = 'tiporeuniao'
    success_url = reverse_lazy("lista_tiposreunioes")

###########################

class ComissaoListView(ListView):
    template_name = "cadastro/comissao_listagem.html"
    model = Comissao
    #ordering = ['descricao']
    context_object_name = "comissoes"


class ComissaoDeleteView(DeleteView):
    template_name = "cadastro/comissao_excluir.html"
    model = Comissao
    fields = '__all__'
    context_object_name = 'comissao'
    success_url = reverse_lazy("lista_comissoes")


class ComissaoCreateView(CreateView):
    template_name = "cadastro/comissao_insere.html"
    model = Comissao
    #fields = '__all__'
    context_object_name = 'comissao'
    form_class = ComissaoForm
    success_url = reverse_lazy("lista_comissoes")


class ComissaoUpdateView(UpdateView):
    template_name = "cadastro/comissao_edita.html"
    model = Comissao
    fields = '__all__'
    context_object_name = 'comissao'
    success_url = reverse_lazy("lista_comissoes")

###########################

class DeputadoListView(ListView):
    template_name = "cadastro/deputado_listagem.html"
    model = Deputado
    context_object_name = "deputados"


class DeputadoCreateView(CreateView):
    template_name = "cadastro/deputado_ficha.html"
    model = Deputado
    #fields = '__all__'
    context_object_name = 'deputado'
    form_class = DeputadoForm
    success_url = reverse_lazy("lista_deputados")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['acao'] = "Insere "
        context['mensagem_aviso'] = "<p class='card-text'>Complete o formulário abaixo para cadastrar uma novo <code>Deputado</code>.</p>"
        context['botao'] = "Cadastrar"

        return context


class DeputadoUpdateView(UpdateView):
    template_name = "cadastro/deputado_ficha.html"
    model = Deputado
    fields = '__all__'
    context_object_name = 'deputado'
    success_url = reverse_lazy("lista_deputados")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['acao'] = "Atualiza "
        context['mensagem_aviso'] = "<p class='card-text'>Faça as alterações necessárias no cadastro do <code>Deputado</code>.</p>"
        context['botao'] = "Atualizar"

        return context


class DeputadoDeleteView(DeleteView):
    template_name = "cadastro/deputado_excluir.html"
    model = Deputado
    fields = '__all__'
    context_object_name = 'deputado'
    success_url = reverse_lazy("lista_deputados")

###########################





#    template_name = "cadastro/cria.html"
#    model = Funcionario
#    form_class = InsereFuncionarioForm
#    success_url = reverse_lazy("cadastro:lista_funcionarios")




###########################

def comissao_edita(request, pk):
    if request.method == "POST":
        form = ComissaoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        comissao = Comissao.objects.get(pk=pk)
        form = ComissaoForm(instance=comissao)
    return render(request, 'cadastro/comissao_edita.html', {'form': form})



###########################


def comissao_edita1(request, comissao_id):
    if request.method == 'POST':
        return HttpResponse("Salvou %s" % comissao_id)
    else:
        comissao = Comissao.objects.filter(id=comissao_id)
        context = {'comissao': comissao}
    return render(request, 'cadastro/comissao_edita.html', context)
        #return HttpResponse("Essa é a pergunta de número %s" % comissao_id)


def comissao_lista(request):
    comissoes = Comissao.objects.order_by("descricao")
    context = {'comissoes': comissoes}
    return render(request, 'cadastro/comissao_listagem.html', context)



def deputado_edita(request, deputado_id):
    return HttpResponse("Essa é a pergunta de número %s" % deputado_id)

def deputado_lista(request):
    deputados = Deputado.objects.order_by("nome")
    context = {'deputados': deputados}
    return render(request, 'cadastro/deputado_listagem.html', context)



def results(request, qual_id):
    response = "Esses são os resultados ....%s" % qual_id
    return HttpResponse(response)


def vote(request, qual_id):
    return HttpResponse("você está votando no número %s" % qual_id)



###########################  INDEX

#class IndexCreateView(TemplateView):
#    template_name = "cadastro/index.html"

#def index(request):
#    return render(request, 'cadastro/index.html')

###########################
