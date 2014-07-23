from django.conf.urls import patterns, url

from sabia import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView, name='index'),
    url(r'^cadastro/$', views.CadastroView, name='cadastro'),
    url(r'^cadastro/novo$', views.CadastrarUsuario, name='cadastrarUsuario'),
    url(r'^home/$', 'sabia.views.Home', name='home'),
    url(r'^sair/$', views.user_logout, name='logout'),
    #url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    #url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)