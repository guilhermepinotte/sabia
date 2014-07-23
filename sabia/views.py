from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse

from sabia.models import *
from django.contrib.auth import authenticate, login, logout

def IndexView(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		
		user = authenticate(username=username, password=password)
		
		if user :
			if user.is_active :
				login(request,user)
				return HttpResponseRedirect('home')
				# return render(request,'sabia/home.html',
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
			
				
def Home(request):
	return render(request,'sabia/home.html', 
		{'classHome': "active"})
