from django.shortcuts import render
from django.views import generic
from django.utils import timezone

from sabia.models import *

def IndexView(request):
	return render(request,'sabia/index.html')

def CadastroView(request):
	return render(request,'sabia/cadastro.html')

def CadastrarUsuario(request):
	if request.method == 'POST':
		try:
			usuario = Usuario()
			usuario.email = request.POST['email']
			usuario.senha = request.POST['senha']
			usuario.nome = request.POST['nome']
			usuario.tipo = request.POST['tipo']
			usuario.ativo = False
			usuario.dataCadastro = timezone.now()	
		except KeyError:
			return render(request,'sabia/cadastro-msg.html',
				{'error_message': "Erro no cadastro"})
		else:
			usuario.save()
			return render(request,'sabia/cadastro-msg.html',
				{'sucess_message': "Usuário cadastrado com sucesso"})
				
			# raise
			# context = 'error'
			# return render(request,'sabia/cadastro-msg.html',context)	