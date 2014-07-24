import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    #Linha necessária. Linkando com UserProfile com User de do Model
    user = models.OneToOneField(User)
    tipo = models.CharField(max_length=255) #tipo só pode assumir dois tipos: [professor] e [aluno]
    
    def ehUsuarioValido(self, tipo):
        return (tipo == 'professor' or tipo == 'aluno')
    
    def __str__(self):
        return self.user.nome
    
class Artigo(models.Model):
    idUsuario = models.OneToOneField(User)
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    descricao = models.TextField()
    dataCadastro = models.DateTimeField('data de cadastro')
     
    def __str__(self):
        return self.titulo
    
class Fichamento(models.Model):
    idUsuario = models.OneToOneField(User)
    idArtigo = models.OneToOneField(Artigo)
    dataCadastro = models.DateTimeField('data de cadastro')
    dataAlteracao = models.DateTimeField('data de alteracao')

class Avaliacao(models.Model):
    idFichamento = models.OneToOneField(Fichamento)
    idUsuario = models.OneToOneField(User)
    consideracao = models.TextField()
    nota = models.FloatField()
    dataAvaliacao = models.DateTimeField('data de avaliacao do artigo')
    replica = models.TextField()
    dataReplica = models.DateTimeField('data de avaliacao do artigo')
    
    def __str__(self):
        return self.nota
    
class Modelo(models.Model):
    idUsuario = models.OneToOneField(User)
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    dataCadastro = models.DateTimeField('data de cadastro')
    
    def __str__(self):
        return self.nome
    
class Campo(models.Model):
    idModelo = models.OneToOneField(Modelo)
    label = models.CharField(max_length=255)
    
    def __str__(self):
        return self.label 
    
class Resposta(models.Model):
    idCampo = models.OneToOneField(Campo)
    idFichamento = models.OneToOneField(Fichamento)
    resposta = models.TextField()
    
    def __str__(self):
        return self.resposta