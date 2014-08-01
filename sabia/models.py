import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    #Linha necessaria. Linkando UserProfile com User do Model
    user = models.OneToOneField(User)
    tipo = models.CharField(max_length=255) #tipo so pode assumir dois tipos: [professor] e [aluno]
    
    def ehUsuarioValido(self, tipo):
        return (tipo == 'professor' or tipo == 'aluno')
    
    def __str__(self):
        return self.user
    
class Modelo(models.Model):
    idUsuario = models.ForeignKey(User)
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    dataCadastro = models.DateTimeField('data de cadastro')
    deletado  = models.BooleanField(default = False)
    
    def __str__(self):
        return self.nome
    
class Artigo(models.Model):
    idUsuario = models.ForeignKey(User)
    idModelo = models.ForeignKey(Modelo)
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    texto = models.TextField()
    dataCadastro = models.DateTimeField('data de cadastro')
     
    def __str__(self):
        return self.titulo
    
class Campo(models.Model):
    idModelo = models.ForeignKey(Modelo)
    label = models.CharField(max_length=255)
    descricao = models.TextField()
    deletado  = models.BooleanField(default = False)
    
    def __str__(self):
        return self.label
    
class Fichamento(models.Model):
    idUsuario = models.ForeignKey(User)
    idArtigo = models.ForeignKey(Artigo)
    nome = models.CharField(max_length=255)
    dataCadastro = models.DateTimeField('data de cadastro')
    dataAlteracao = models.DateTimeField('data de alteracao')
    
class Avaliacao(models.Model):
    idFichamento = models.ForeignKey(Fichamento)
    idUsuario = models.ForeignKey(User)
    consideracao = models.TextField()
    nota = models.FloatField()
    dataAvaliacao = models.DateTimeField('data de avaliacao do artigo')
    replica = models.TextField()
    dataReplica = models.DateTimeField('data de avaliacao do artigo')
    
    def __str__(self):
        return self.nota
    
class Resposta(models.Model):
    idCampo = models.ForeignKey(Campo)
    idFichamento = models.ForeignKey(Fichamento)
    resposta = models.TextField()
    
    def __str__(self):
        return self.resposta
