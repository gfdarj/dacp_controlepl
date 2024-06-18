from django import forms
from .models import Comissao, Deputado, TipoReuniao, Projeto, ControleReuniao, Tramitacao

class ComissaoForm(forms.ModelForm):
  class Meta:
    model = Comissao
    fields = ["descricao", "ativo", "data_atualizacao",]
    labels = {"descricao": "Descrição", "ativo": "Ativo", "data_atualizacao": "Última Atualização",}

    # Campos que não estarão no form
    #exclude = ['tempo_de_servico']


class DeputadoForm(forms.ModelForm):
  class Meta:
    model = Deputado
    fields = ["nome", "partido", "ativo", "data_atualizacao",]
    labels = {"nome": "Nome", "partido": "Partido", "ativo": "Ativo", "data_atualizacao": "Última Atualização",}


class TipoReuniaoForm(forms.ModelForm):
  class Meta:
    model = TipoReuniao
    fields = ["sigla", "descricao", "ativo", "data_atualizacao",]
    labels = {"sigla": "Sigla", "descricao": "Descrição", "ativo": "Ativo", "data_atualizacao": "Última Atualização",}


class ProjetoForm(forms.ModelForm):
  class Meta:
    model = Projeto
    fields = ["ano", "numero", "ementa", "ementa", "autor", "data_atualizacao",]
    labels = {"ano": "Ano", "numero": "Número", "ementa": "Ementa", "autor": "Autor", "data_atualizacao": "Última Atualização",}
    widgets = {
        'ementa': forms.Textarea(attrs={"rows":3, "cols":10}),
    }

class ControleReuniaoForm(forms.ModelForm):
  class Meta:
    model = ControleReuniao
    fields = ["comissao", "ordem", "tiporeuniao", "data_reuniao", "tem_edital_assinado", "data_edital_do", "tem_presenca_assinada", "tem_ata_assinada",
        "data_ata_do", "tem_parecer", "tem_parecer_assinado", "data_parecer_do", "tem_deliberacao", "tem_deliberacao_assinada",
        "tem_conclusao", "tem_conclusao_assinada", "observacao", "concluido", "data_atualizacao",
    ]
    labels = {"comissao": "Comissão", "ordem" : "Ordem", "tiporeuniao" : "Tipo de Reunião",
              "data_reuniao" : "Data da Reunião", "tem_edital_assinado" : "Tem Edital Assinado", "data_edital_do" : "Data do Edital D.O.",
              "tem_presenca_assinada" : "Tem Presença Assinada", "tem_ata_assinada" : "Tem Ata Assinada",
              "data_ata_do" : "Data da ATA no D.O.", "tem_parecer" : "Tem Parecer", "tem_parecer_assinado" : "Tem Parecer Assinado",
              "data_parecer_do" : "Data do Parecer no D.O.", "tem_deliberacao" : "Tem Deliberação", "tem_deliberacao_assinada" : "Tem Deliberação Assinada",
              "tem_conclusao" : "Tem Conclusão", "tem_conclusao_assinada" : "Tem Conclusão Assinada", "observacao" : "Observação",
              "concluido" : "Concluído", "data_atualizacao" : "Data de Atualização",
    }

    def is_valid(self):
        valid = super(ControleReuniaoForm, self).is_valid()
        id_comissao = self.cleaned_data.get('comissao')

        if id_comissao is None:
            self.add_error('É necessário informar a Comissão.')
            valid = False

        return valid

    def add_error(self, message):
        errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        errors.append(message)


class TramitacaoForm(forms.ModelForm):
  class Meta:
    model = Tramitacao
    fields = ["data_tramitacao", "data_atualizacao",]
    labels = {"data_tramitacao": "Data da Tramitacao", "data_atualizacao": "Última Atualização",}


#  descricao = forms.CharField(
#    label='Descrição',
#    max_length=200
#  )
#  ativo = forms.BooleanField(
#    label='Ativo'
#  )
#  data_atualizacao = forms.DateTimeField(
#    label="Última Atualização"
#  )
