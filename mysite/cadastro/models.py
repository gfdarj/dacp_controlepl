from django.db import models
from django.utils import timezone
from django.db.models.functions import Concat
from django.db.models import Value, CharField
#from google.appengine.ext import ndb

# Create your models here.

#class Person(ndb.Model):
#  name = ndb.StringProperty()
#  age = ndb.IntegerProperty()



class Deputado(models.Model):
    nome = models.CharField(max_length=200)
    partido = models.CharField(max_length=50, default=None)
    data_atualizacao = models.DateTimeField('Data Atualização', default=timezone.now)
    ativo = models.BooleanField(default=True)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome

    def Ativo(self):
        if self.ativo:
            return "Ativo"
        else:
            return "Inativo"

    def somente_ativos(self):
        return self.ativo == True

    def somente_inativos(self):
        return self.ativo == False


class Comissao(models.Model):
    descricao = models.CharField(max_length=200)
    data_atualizacao = models.DateTimeField('Data Atualização', default=timezone.now)
    ativo = models.BooleanField(default=True)

    class Meta:
        ordering = ['descricao']

    def __str__(self):
        return self.descricao

    def somente_ativos(self):
        return self.ativo == True

    def somente_inativos(self):
        return self.ativo == False

    def Ativo(self):
        if self.ativo:
            return "Ativo"
        else:
            return "Inativo"


class TipoReuniao(models.Model):
    sigla = models.CharField(max_length=10, default=None)
    descricao = models.CharField(max_length=100, default=None)
    data_atualizacao = models.DateTimeField('Data Atualização', default=timezone.now)
    ativo = models.BooleanField(default=True)

    class Meta:
        ordering = ['descricao']

    def __str__(self):
        return self.descricao

    def Ativo(self):
        if self.ativo:
            return "Ativo"
        else:
            return "Inativo"

    def somente_ativos(self):
        return self.ativo == True

    def somente_inativos(self):
        return self.ativo == False


class Projeto(models.Model):
    PERGUNTA_CHOICES = (
        ("S", "Sim"),
        ("N", "Não"),
    )
    ano = models.IntegerField(null=False, blank=False)
    numero = models.IntegerField(null=False, blank=False)
    ementa = models.CharField(max_length=2000)
    autor = models.ForeignKey(Deputado, on_delete=models.PROTECT, related_name='autor_projeto', default=None)
    relator = models.ForeignKey(Deputado, on_delete=models.PROTECT, related_name='relator_projeto', default=None, blank=True, null=True)
    observacao = models.CharField(max_length=2000, default=None, null=True)
    tem_parecer = models.BooleanField(default=False, null=True)
    reuniao = models.IntegerField(default=None, null=True)
    esta_na_comissao = models.CharField(choices=PERGUNTA_CHOICES, max_length=1, default="N", null=True)
    parecer_notes = models.CharField(choices=PERGUNTA_CHOICES, max_length=1, default="N", null=True)
    numero_lei = models.CharField(max_length=50, blank=None, null=True)
    data_atualizacao = models.DateTimeField('Data Atualização', default=timezone.now)

    class Meta:
        ordering = ['-ano', '-numero']
        unique_together = ('ano', 'numero',)

    def __str__(self):
        return str(self.numero) + "/" + str(self.ano)


class Tramitacao(models.Model):
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    comissao = models.ForeignKey(Comissao, on_delete=models.PROTECT, null=True)
    descricao = models.CharField(max_length=2000, default=None)
    data_tramitacao = models.DateTimeField('Data Tramitação', default=timezone.now)
    observacao = models.CharField(max_length=2000, default=None, null=True)
    data_atualizacao = models.DateTimeField('Data Atualização', default=timezone.now)

    class Meta:
        ordering = ['-data_tramitacao']

    def __str__(self):
        return str(self.projeto) + "/" + str(self.comissao)


class ControleReuniao(models.Model):
    PERGUNTA_CHOICES = (
        ("S", "Sim"),
        ("N", "Não"),
        ("NA", "N/A")
    )
    comissao = models.ForeignKey(Comissao, on_delete=models.PROTECT)
    ordem = models.IntegerField(default=None)
    tiporeuniao = models.ForeignKey(TipoReuniao, on_delete=models.PROTECT)
    data_reuniao = models.DateTimeField('Data Reunião', default=timezone.now)
    tem_edital_assinado = models.CharField(choices=PERGUNTA_CHOICES, blank=False, null=False, max_length=2)
    data_edital_do = models.DateTimeField('Data Edital D.O.', default=timezone.now)
    tem_presenca_assinada = models.CharField(choices=PERGUNTA_CHOICES, blank=False, null=False, max_length=2)
    tem_ata_assinada = models.CharField(choices=PERGUNTA_CHOICES, blank=False, null=False, max_length=2)
    data_ata_do = models.DateTimeField('Data Ata D.O.', default=timezone.now)
    tem_parecer = models.CharField(choices=PERGUNTA_CHOICES, blank=False, null=False, max_length=2)
    tem_parecer_assinado = models.CharField(choices=PERGUNTA_CHOICES, blank=False, null=False, max_length=2)
    data_parecer_do = models.DateTimeField('Data Parecer D.O.', default=timezone.now)
    tem_deliberacao = models.CharField(choices=PERGUNTA_CHOICES, blank=False, null=False, max_length=2)
    tem_deliberacao_assinada = models.CharField(choices=PERGUNTA_CHOICES, blank=False, null=False, max_length=2)
    tem_conclusao = models.CharField(choices=PERGUNTA_CHOICES, blank=False, null=False, max_length=2)
    tem_conclusao_assinada = models.CharField(choices=PERGUNTA_CHOICES, blank=False, null=False, max_length=2)
    observacao = models.TextField()
    concluido = models.BooleanField(default=False, blank=False, null=False)
    data_atualizacao = models.DateTimeField('Data Atualização', default=timezone.now)

    def __str__(self):
        return str(self.ordem) + "/" + str(self.tiporeuniao)
