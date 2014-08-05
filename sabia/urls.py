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
    url(r'^fichamentos/(?P<get_id>\d+)/novo$', views.NovoFichamento, name='novofichamento'),
    url(r'^fichamentos/(?P<get_id>\d+)/novo/new$', views.CadastrarFichamento, name='cadastrarFichamento'),
    url(r'^fichamentos/(?P<get_id>\d+)/$', views.verFichamento, name='verfichamento'),
    url(r'^fichamentos/(?P<get_id>\d+)/edita$', views.editaFichamento, name='editafichamento'),
    url(r'^fichamentos/(?P<get_id>\d+)/edita/fich$', views.editarFichamento, name='alterafichamento'),
    url(r'^fichamentos/(?P<get_id>\d+)/exc$', views.excluirFichamento, name='excluirfichamento'),
    
    url(r'^fichamentos/modelos/$', views.Modelos, name='modelos'),
    url(r'^fichamentos/modelos/novo$', views.novoModelo, name='novomodelo'),
    url(r'^fichamentos/modelos/(?P<get_id>\d+)/ver$', views.verModelo, name='vermodelo'),
    url(r'^fichamentos/modelos/(?P<get_id>\d+)/edita$', views.editaModelo, name='editamodelo'),  
    url(r'^fichamentos/modelos/ajaxmodelo$', views.ajaxModelo, name='ajaxmodelo'),  
    
    #Artigos
    url(r'^artigos/$', views.Artigos, name='artigos'),
    url(r'^artigos/novo$', views.novoArtigo, name='novoartigo'),
    url(r'^artigos/(?P<get_id>\d+)/ver$', views.VerArtigo, name='verartigo'),
    url(r'^artigos/(?P<get_id>\d+)/edita$', views.EditarArtigoView, name='editarartigo'),
    url(r'^artigos/(?P<get_id>\d+)/edita/art$', views.EditarArtigo, name='alterarartigo'),
    url(r'^artigos/(?P<get_id>\d+)/exc$', views.ExcluirArtigo, name='excluirartigo'),
    url(r'^artigos/novo/new$', views.CadastrarArtigo, name='cadastrarArtigo'),
    
    #Avaliacoes
    url(r'^avaliacoes/$', views.Avaliacoes, name='avaliacoes'),
    
    
    # url(r'^artigos/novo$', views.CadastrarArtigo, name='cadastrarArtigo'),
    #url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    #url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)