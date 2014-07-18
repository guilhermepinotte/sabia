import datetime
from django.utils import timezone
from django.db import models

class Usuario(models.Model):
    email = models.CharField(max_length=255)
    senha = models.CharField(max_length=255)
    nome = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255) #tipo só pode assumir dois tipos: Professor e Aluno
    ativo = models.BooleanField(default=False)
    dataCadastro = models.DateTimeField('data de cadastro')
    
    def ehUsuarioValido(self, tipo):
        return (tipo == 'professor' or tipo == 'aluno')
    
    def __str__(self):
        return self.nome

class GrupoDeUsuarios(models.Model):
    nome = models.CharField(max_length=255)
    interesses = models.CharField(max_length=255)
    descricao = models.TextField()
    dataCadastro = models.DateTimeField('data de cadastro')
    
    def __str__(self):
        return self.nome
    
class GrupoUsuarios(models.Model):
    idUsuario = models.ForeignKey(Usuario)
    idGrupoUsuarios = models.ForeignKey(GrupoDeUsuarios)
    dataInscricao = models.DateTimeField('data de inscricao no grupo de usuarios')
    
class Artigo(models.Model):
    idUsuario = models.ForeignKey(Usuario)
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    descricao = models.TextField()
    dataCadastro = models.DateTimeField('data de cadastro')
     
    def __str__(self):
        return self.titulo
    
class Fichamento(models.Model):
    idUsuario = models.ForeignKey(Usuario)
    idArtigo = models.ForeignKey(Artigo)
    dataCadastro = models.DateTimeField('data de cadastro')
    dataAlteracao = models.DateTimeField('data de alteracao')

class Avaliacao(models.Model):
    idFichamento = models.ForeignKey(Fichamento)
    idUsuario = models.ForeignKey(Usuario)
    consideracao = models.TextField()
    nota = models.FloatField()
    dataAvaliacao = models.DateTimeField('data de avaliacao do artigo')
    replica = models.TextField()
    dataReplica = models.DateTimeField('data de avaliacao do artigo')
    
    def __str__(self):
        return self.nota
    
class Modelo(models.Model):
    idUsuario = models.ForeignKey(Usuario)
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    dataCadastro = models.DateTimeField('data de cadastro')
    
    def __str__(self):
        return self.nome
    
class Campo(models.Model):
    idModelo = models.ForeignKey(Usuario)
    label = models.CharField(max_length=255)
    
    def __str__(self):
        return self.label 
    
class Resposta(models.Model):
    idCampo = models.ForeignKey(Campo)
    idFichamento = models.ForeignKey(Fichamento)
    resposta = models.TextField()
    
    def __str__(self):
        return self.resposta