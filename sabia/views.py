# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse

from sabia.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

import pprint

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

			#Cadastrar Modelo de Fichamento Default
			CadastrarModeloDefault(usuario)

			userprofile.user = usuario
			userprofile.save()
			return render(request,'sabia/cadastro-msg.html',
				{'sucess_message': "Usuário cadastrado com sucesso"})

#
#  H O M E
#
@login_required		
def Home(request):
	conteudo = 'sabia/home/home.html'
	artigos = Artigo.objects.filter(idUsuario=request.user.id)
	modelos = Modelo.objects.filter(idUsuario=request.user.id)

	return render(request,'sabia/painel.html', 
		{'activeHome': "active",
		'conteudo': conteudo,
		'artigos': artigos,
		'modelos': modelos})

#
#  F I C H A M E N T O
#
@login_required	
def Fichamentos(request):
	error_message = False
	success_message = False
	error_message_alt = False
	success_message_alt = False
	error_message_exc = False
	success_message_exc = False
	if 'error_message' in request.session:
		error_message = request.session['error_message']
		request.session['error_message'] = False
	if 'success_message' in request.session:
		success_message = request.session['success_message']
		request.session['success_message'] = False
	if 'success_message_alt' in request.session:
		success_message_alt = request.session['success_message_alt']
		request.session['success_message_alt'] = False
	if 'error_message_alt' in request.session:
		error_message_alt = request.session['error_message_alt']
		request.session['error_message_alt'] = False
	if 'success_message_exc' in request.session:
		success_message_exc = request.session['success_message_exc']
		request.session['success_message_exc'] = False
	if 'error_message_exc' in request.session:
		error_message_exc = request.session['error_message_exc']
		request.session['error_message_exc'] = False

	conteudo = 'sabia/fichamento/lista_fichamentos.html'
	fichamentos = Fichamento.objects.filter(idUsuario=request.user.id)
	artigos = Artigo.objects.filter(idUsuario=request.user.id)
	return render(request,'sabia/painel.html',
				{'activeFichamentos': "active",
				'fichamentos': fichamentos,
				'artigos': artigos,
				'conteudo': conteudo,
				'success_msg': success_message,
				'error_msg': error_message,
				'success_msg_alt': success_message_alt,
				'error_msg_alt': error_message_alt,
				'success_msg_exc': success_message_exc,
				'error_msg_exc': error_message_exc})

@login_required	
def NovoFichamento(request,get_id):	
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
	#Buscar mensagem para mostrar ao usuário	
	if 'msg_success' in request.session:
		msg = request.session['msg_success']
		request.session['msg_success'] = False
	else:
		msg=False
	
	#Buscar Modelos Salvos	
	meus_modelos = Modelo.objects.filter(idUsuario = request.user, deletado = False)
	tam1 = len(meus_modelos)
	
	#Buscar os demais modelos
	todos_modelos = Modelo.objects.exclude(idUsuario=request.user).filter(deletado = False)
	tam2 = len(todos_modelos)			
	
	if  tam1 > 0:		
		meus_modelosvazio = False
	else:
		meus_modelosvazio = True
			
	if  tam2 > 0:
		todos_modelosvazio = False
	else:
		todos_modelosvazio = True
			
	conteudo = 'sabia/fichamento/lista_modelo.html'
	return render(request,'sabia/painel.html', 
		{'activeFichamentos': "active",
		'msg_success':msg,
		'meus_modelos':meus_modelos,
		'meus_modelosvazio':meus_modelosvazio,
		'todos_modelos':todos_modelos,
		'todos_modelosvazio':todos_modelosvazio,
		
		'conteudo': conteudo})
	
@login_required	
def novoModelo(request):
	conteudo = 'sabia/fichamento/novo_modelo.html'	
	
	if request.method == 'POST':
		#Nome do Modelo		
		modelonome      = request.POST['modelonome']
		modelodescricao = request.POST['modelodescricao']
		
		modelo = Modelo()
		modelo.idUsuario    = request.user
		modelo.nome         = modelonome
		modelo.descricao    = modelodescricao
		modelo.dataCadastro = timezone.now()
		modelo.save()
				
		#Campos
		qtd = int(request.POST['qtdcampos'])
		for i in range(1,qtd+1):
			namecampo = 'camponome'+str(i)
			descricao = 'campodescricao'+str(i)			
			if (namecampo in request.POST):									
				campo = Campo()
				campo.idModelo  = modelo
				campo.label     = request.POST[namecampo]
				campo.descricao = request.POST[descricao]		
				campo.save()
				
		request.session['msg_success']='<b>Modelo:</b> O novo modelo foi criado com sucesso.'
		return HttpResponseRedirect("/sabia/fichamentos/modelos")
		
	return render(request,'sabia/painel.html', 
		{'activeFichamentos': "active",		
		'conteudo': conteudo})
	
@login_required	
def editaModelo(request,get_id):
	conteudo = 'sabia/fichamento/edita_modelo.html'
		
	if request.method == 'POST':		
		try:
			#Nome do Modelo		
			modeloid        = request.POST['modeloid']
			modelonome      = request.POST['modelonome']
			modelodescricao = request.POST['modelodescricao']		
			modelo = Modelo.objects.get(id=modeloid)
						
			#modelo.idUsuario    = request.user
			modelo.nome         = modelonome
			modelo.descricao    = modelodescricao
			modelo.dataCadastro = timezone.now()
			modelo.save()		
			
			#Campos - montar uma lista
			qtd = int(request.POST['qtdcampos'])
			#Nome e Descrição dos campos
			for i in range(1,qtd+1):
				inputcampoid   = 'campoid'+str(i)
				inputcamponame = 'camponome'+str(i)
				inputdescricao = 'campodescricao'+str(i)
				if (inputcamponame in request.POST):
					campoid = request.POST[inputcampoid]					
					if campoid == 'camponovo':
						#Novo campo adicionado na edição		
						campo = Campo()						
						campo.idUsuario = request.user
						campo.dataCadastro = timezone.now()
					else:
						#O campo foi só alterado
						campo = Campo.objects.get(id=campoid)		
					
					campo.idModelo  = modelo
					campo.label     = request.POST[inputcamponame]
					campo.descricao = request.POST[inputdescricao]		
					campo.save()
					
			request.session['msg_success']='<b>Modelo:</b> As alterações foram salvas com sucesso.'
			return HttpResponseRedirect("/sabia/fichamentos/modelos")
		except Exception as e:
			print (e)
			request.session['msg_danger']='<b>Modelo:</b> As alterações <b>não</b> foram salvas.'
	
	#Exibir página de Edição
	modelo = Modelo.objects.get(id = get_id)
	campos = Campo.objects.filter(idModelo = get_id , deletado=False)
	qtdcampo = len(campos)		
	
	return render(request,'sabia/painel.html', 
		{'activeFichamentos': "active",
		'modelo':modelo,
		'campos':campos,
		'qtdcampo':qtdcampo,
		'conteudo': conteudo,
		'get_id':get_id})	

@login_required 
@csrf_exempt
def ajaxModelo(request):
	try:
		if request.method == 'POST' and request.is_ajax():
			op = request.POST['op']
			
			if op == "apagar-campo":
				campoid = int(request.POST['campoid'])			
				campo = Campo.objects.get(id=campoid)
				campo.deletado = True
				campo.save()				
				return HttpResponse("True")
			
			elif op == "apagar-modelo":
				modeloid = int(request.POST['modeloid'])				
				modelo = Modelo.objects.get(id=modeloid)
				
				modelo.deletado = True
				modelo.save()				
				return HttpResponse("True")
			
	except Exception as e:		
		return HttpResponse('False')

@login_required	
def verModelo(request,get_id):
	conteudo = 'sabia/fichamento/ver_modelo.html'
	return render(request,'sabia/painel.html', 
		{'activeFichamentos': "active",
		'conteudo': conteudo,
		'get_id':get_id})	

def CadastrarModeloDefault(usuario):
	modelo = Modelo()
	modelo.idUsuario = usuario
	modelo.nome = 'Default'
	modelo.descricao = 'Modelo Default de Fichamento'
	modelo.dataCadastro = timezone.now()
	modelo.save()
			
	#Campos
	campo1 = Campo()
	campo1.idModelo = modelo
	campo1.label     = 'Pontos Positivos'
	campo1.descricao = 'Aqui você deve descrever os pontos positivos encontrados na leitura do artigo'
	campo1.save()

	campo2 = Campo()
	campo2.idModelo = modelo
	campo2.label     = 'Pontos Negativos'
	campo2.descricao = 'Aqui você deve descrever os pontos negativos encontrados na leitura do artigo'
	campo2.save()

#
#  A R T I G O S
#
@login_required	
def Artigos(request):
	error_message = False
	success_message = False
	error_message_alt = False
	success_message_alt = False
	error_message_exc = False
	success_message_exc = False
	if 'error_message' in request.session:
		error_message = request.session['error_message']
		request.session['error_message'] = False
	if 'success_message' in request.session:
		success_message = request.session['success_message']
		request.session['success_message'] = False
	if 'success_message_alt' in request.session:
		success_message_alt = request.session['success_message_alt']
		request.session['success_message_alt'] = False
	if 'error_message_alt' in request.session:
		error_message_alt = request.session['error_message_alt']
		request.session['error_message_alt'] = False
	if 'success_message_exc' in request.session:
		success_message_exc = request.session['success_message_exc']
		request.session['success_message_exc'] = False
	if 'error_message_exc' in request.session:
		error_message_exc = request.session['error_message_exc']
		request.session['error_message_exc'] = False

	conteudo = 'sabia/artigo/lista_artigos.html'
	artigos = Artigo.objects.filter(idUsuario=request.user.id)
	return render(request,'sabia/painel.html',
				{'activeArtigos': "active",
				'artigos': artigos,
				'conteudo': conteudo,
				'success_msg': success_message,
				'error_msg': error_message,
				'success_msg_alt': success_message_alt,
				'error_msg_alt': error_message_alt,
				'success_msg_exc': success_message_exc,
				'error_msg_exc': error_message_exc})

@login_required	
def novoArtigo(request):
	modelos = Modelo.objects.filter(idUsuario=request.user.id)
	conteudo = 'sabia/artigo/novo_artigo.html'
	return render(request,'sabia/painel.html',
				{'activeArtigos': "active",
				'modelos': modelos,
				'conteudo': conteudo})

@login_required	
def CadastrarArtigo(request):
	if request.method == 'POST':
		try:
			artigo = Artigo()
			artigo.idUsuario = request.user
			artigo.titulo = request.POST['titulo']
			artigo.autor = request.POST['autor']
			artigo.texto = request.POST['texto']
			artigo.dataCadastro = timezone.now()

			#modelo
			modelo = request.POST['modelo']
			artigo.idModelo = Modelo.objects.get(id=int(modelo))

		except KeyError as a:
			request.session['error_message'] = "Erro no cadastro"
			return HttpResponseRedirect('/sabia/artigos')
		else:
			artigo.save()
			request.session['success_message'] = "Artigo cadastrado com sucesso!"
			return HttpResponseRedirect('/sabia/artigos')

@login_required	
def VerArtigo(request,get_id):
	artigo = Artigo.objects.get(id=int(get_id))
	conteudo = 'sabia/artigo/ver_artigo.html'
	return render(request,'sabia/painel.html', 
		{'activeArtigos': "active",
		'conteudo': conteudo,
		'artigo': artigo})

@login_required	
def EditarArtigoView(request,get_id):
	artigo = Artigo.objects.get(id=int(get_id))
	modelos = Modelo.objects.filter(idUsuario=request.user.id)

	modelosAux = []
	for modelo in modelos:
	 	if modelo.id != artigo.idModelo.id:
	 		modelosAux.append(modelo)

	conteudo = 'sabia/artigo/alterar_artigo.html' 		
	return render(request,'sabia/painel.html', 
		{'activeArtigos': "active",
		'conteudo': conteudo,
		'modelos': modelosAux,
		'artigo': artigo})

@login_required	
def EditarArtigo(request,get_id):
	if request.method == 'POST':
		try:
			artigo = Artigo.objects.get(id=int(get_id))
			artigo.titulo = request.POST['titulo']
			artigo.autor = request.POST['autor']
			artigo.texto = request.POST['texto']

			#modelo
			modelo = request.POST['modelo']
			artigo.idModelo = Modelo.objects.get(id=int(modelo))
		except KeyError as a:
			request.session['error_message_alt'] = "Erro ao alterar artigo"
			return HttpResponseRedirect('/sabia/artigos')
		else:
			artigo.save()
			request.session['success_message_alt'] = "Artigo alterado com sucesso!"
			return HttpResponseRedirect('/sabia/artigos')

@login_required
def ExcluirArtigo(request,get_id):
	try:
		artigo = Artigo.objects.get(id=int(get_id))
	except KeyError as a:
			request.session['error_message_exc'] = "Erro ao excluir artigo"
			return HttpResponseRedirect('/sabia/artigos')
	else:
		artigo.delete()
		request.session['success_message_exc'] = "Artigo excluído com sucesso!"
		return HttpResponseRedirect('/sabia/artigos')
#
#  A V A L I A C A O
#
@login_required	
def Avaliacoes(request):
	conteudo = 'sabia/avaliacao/lista_avaliacao.html'
	return render(request,'sabia/painel.html', 
		{'activeAvaliacoes': "active",
		'conteudo': conteudo})	

