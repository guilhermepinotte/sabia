from django.conf.urls import patterns, url

from sabia import views

urlpatterns = patterns('',
    #Index
    url(r'^$', views.IndexView, name='index'),    
    url(r'^cadastro/$', views.CadastroView, name='cadastro'),
    url(r'^cadastro/novo$', views.CadastrarUsuario, name='cadastrarUsuario'),
    url(r'^sair/$', views.user_logout, name='logout'),
    
    #Painel    
    url(r'^home/$', views.Home, name='home'),
    
    #Fichamento
    url(r'^fichamentos/$', views.Fichamentos, name='fichamentos'),
    url(r'^fichamentos/novo$', views.novoFichamento, name='novofichamento'),
    url(r'^fichamentos/(?P<get_id>\d+)/ver', views.verFichamento, name='verfichamento'),
    url(r'^fichamentos/(?P<get_id>\d+)/edita$', views.editaFichamento, name='editafichamento'),
    
    url(r'^fichamentos/modelo/$', views.Modelos, name='modelo'),    
    url(r'^fichamentos/modelo/novo$', views.novoModelo, name='novomodelo'),
    url(r'^fichamentos/modelo/(?P<get_id>\d+)/ver$', views.verModelo, name='vermodelo'),
    url(r'^fichamentos/modelo/(?P<get_id>\d+)/edita$', views.editaModelo, name='editamodelo'),    
    
    #Artigos
    url(r'^artigos/$', views.Artigos, name='artigos'),
    url(r'^artigos/novo$', views.novoArtigo, name='novoartigo'),
    url(r'^artigos/novo/new$', views.CadastrarArtigo, name='cadastrarArtigo'),
    
    #Avaliacoes
    url(r'^avaliacoes/$', views.Avaliacoes, name='avaliacoes'),
    
    
    # url(r'^artigos/novo$', views.CadastrarArtigo, name='cadastrarArtigo'),
    #url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    #url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)