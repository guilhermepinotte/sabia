# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse

from sabia.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def IndexView(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user :
			if user.is_active :
				login(request,user)
				return HttpResponseRedirect('home')
				# return render(request,'sabia/painel.html',
				# 	{'classHome': "active"})
		else:
			return render(request,'sabia/index.html',{'error_message':'Usuario nao ativo'})
	else:		
		return render(request,'sabia/index.html')

def user_logout(request):
	logout(request)
	return render(request,'sabia/index.html')

def CadastroView(request):
	return render(request,'sabia/cadastro.html')

def CadastrarUsuario(request):
	registrado = False
	if request.method == 'POST':
		try:
			#Campos da table auth_user (django)
			usuario = User()
			usuario.email = request.POST['email']
			usuario.set_password(request.POST['senha'])		
			usuario.name = request.POST['nome']
			usuario.username = request.POST['nome']					
			usuario.tipo = request.POST['tipo']				
			usuario.dataCadastro = timezone.now()
			
			#Campos da sabia_userprofile
			userprofile = UserProfile()			
			userprofile.tipo = request.POST['tipo']						
				
		except KeyError:
			return render(request,'sabia/cadastro-msg.html',
				{'error_message': "Erro no cadastro"})
		else:
			usuario.save()
			userprofile.user = usuario
			userprofile.save()
			registrado = True
			return render(request,'sabia/cadastro-msg.html',
				{'sucess_message': "Usuário cadastrado com sucesso"})

#
#  H O M E
#
@login_required		
def Home(request):
	conteudo = 'sabia/home/home.html'
	return render(request,'sabia/painel.html', 
		{'activeHome': "active",
		'conteudo': conteudo})

#
#  F I C H A M E N T O
#
@login_required	
def Fichamentos(request):	
	conteudo = 'sabia/fichamento/lista_fichamentos.html'
	return render(request,'sabia/painel.html', 
		{'activeFichamentos': "active",
		'conteudo': conteudo})

@login_required	
def novoFichamento(request):
	conteudo = 'sabia/fichamento/novo_fichamento.html'
	return render(request,'sabia/painel.html', 
		{'activeFichamentos': "active",
		'conteudo': conteudo})

@login_required	
def verFichamento(request,get_id):	
	conteudo = 'sabia/fichamento/ver_fichamento.html'
	return render(request,'sabia/painel.html', 
		{'activeFichamentos': "active",
		'conteudo': conteudo,
		'get_id':get_id})	

@login_required	
def editaFichamento(request,get_id):	
	conteudo = 'sabia/fichamento/edita_fichamento.html'
	return render(request,'sabia/painel.html', 
		{'activeFichamentos': "active",
		'conteudo': conteudo,
		'get_id':get_id})
	
#### MODELOS
@login_required	
def Modelos(request):
	conteudo = 'sabia/fichamento/lista_modelo.html'
	return render(request,'sabia/painel.html', 
		{'activeFichamentos': "active",
		'conteudo': conteudo})
	
@login_required	
def novoModelo(request):
	conteudo = 'sabia/fichamento/novo_modelo.html'
	return render(request,'sabia/painel.html', 
		{'activeFichamentos': "active",
		'conteudo': conteudo})
	
@login_required	
def editaModelo(request,get_id):
	conteudo = 'sabia/fichamento/edita_modelo.html'
	return render(request,'sabia/painel.html', 
		{'activeFichamentos': "active",
		'conteudo': conteudo,
		'get_id':get_id})	
	
@login_required	
def verModelo(request,get_id):
	conteudo = 'sabia/fichamento/ver_modelo.html'
	return render(request,'sabia/painel.html', 
		{'activeFichamentos': "active",
		'conteudo': conteudo,
		'get_id':get_id})	
	
#
#  A R T I G O S
#
@login_required	
def Artigos(request):
	conteudo = 'sabia/artigo/lista_artigos.html'
	artigos = Artigo.objects.filter(idUsuario=request.user.id)
	return render(request,'sabia/painel.html',
				{'activeArtigos': "active",
				'artigos': artigos,
				'conteudo': conteudo})	

@login_required	
def novoArtigo(request):
	conteudo = 'sabia/artigo/novo_artigo.html'	
	return render(request,'sabia/painel.html',
				{'activeArtigos': "active",
				'conteudo': conteudo})
			
#
#  A V A L I A C A O
#
@login_required	
def Avaliacoes(request):
	conteudo = 'sabia/avaliacao/lista_avaliacao.html'
	return render(request,'sabia/painel.html', 
		{'activeAvaliacoes': "active",
		'conteudo': conteudo})	

