# -*- coding: utf8 -*-
from django.contrib import admin

from sabia.models import *
'''    
class ArtigoAdmin(admin.ModelAdmin):
    fieldsets = [
        (u'Proprietário', {'fields': ['idUsuario_id'], 'classes': ['collapse']}),
        ( 'Artigo',       {'fields': ['titulo', 'autor', 'descricao'], 'classes': ['collapse']}),
        ( 'Envio',        {'fields': ['dataCadastro'], 'classes': ['collapse']})
    ]
    list_display = ('id', 'titulo', 'autor', 'idUsuario_id', 'dataCadastro')

class FichamentoAdmin(admin.ModelAdmin): 
    fieldsets = [
        (u'Proprietário', {'fields': ['idUsuario_id'], 'classes': ['collapse']}),
        ( 'Artigo',       {'fields': ['idArtigo_id'], 'classes': ['collapse']}),
        (u'Histórico',    {'fields': ['dataCadastro', 'dataAlteracao'], 'classes': ['collapse']})
    ]
    list_display = ('id', 'idUsuario_id', 'idArtigo_id', 'dataCadastro', 'dataAlteracao')

class CampoAdmin(admin.ModelAdmin):
    fieldsets = [
        (u'Identificação',  {'fields': ['idModelo_id'], 'classes': ['collapse']}),
        ( 'Pergunta',       {'fields': ['label'], 'classes': ['collapse']})
    ]
    list_display = ('id', 'idModelo_id', 'label')

class CampoInline(admin.TabularInline):
    model = Campo
    extra = 1

class RespostaAdmin(admin.ModelAdmin): 
    fieldsets = [
        (u'Identificação',  {'fields': ['idFichamento'], 'classes': ['collapse']}),
        ( 'Resposta',       {'fields': ['idCampo_id', 'resposta'], 'classes': ['collapse']})
    ]
    list_display = ('id', 'idFichamento', 'idCampo_id', 'resposta')

class RespostaInline(admin.TabularInline): 
    model = Resposta
    extra = 1

class ModeloAdmin(admin.ModelAdmin):
    fieldsets = [
        (u'Proprietário',  {'fields': ['idUsuario_id'], 'classes': ['collapse']}),
        (u'Identificação', {'fields': ['nome', 'descricao','dataCadastro'], 'classes': ['collapse']})
    ]
    list_display = ('id', 'nome', 'idUsuario_id', 'dataCadastro')
    #inlines = [CampoInline] #inlines = [RespostaInline]
    
class AvaliacaoAdmin(admin.ModelAdmin): 
    fieldsets = [
        (u'Identificação', {'fields': ['idFichamento'], 'classes': ['collapse']}),
        (u'Proprietário',  {'fields': ['idUsuario'], 'classes': ['collapse']}),
        (u'Avaliação',  {'fields': ['consideracao', 'nota', 'dataAvaliacao'], 'classes': ['collapse']}),
        ( 'Replica',  {'fields': ['replica', 'dataReplica'], 'classes': ['collapse']}),
    ]
    list_display = ('id', 'idFichamento', 'idUsuario', 'nota')

admin.site.register(Artigo, ArtigoAdmin)
admin.site.register(Fichamento, FichamentoAdmin)
admin.site.register(Modelo, ModeloAdmin)
admin.site.register(Campo, CampoAdmin)
admin.site.register(Resposta, RespostaAdmin)
admin.site.register(Avaliacao, AvaliacaoAdmin)
'''
admin.site.register(Artigo)
admin.site.register(Fichamento)
admin.site.register(Modelo)
admin.site.register(Campo)
admin.site.register(Resposta)
admin.site.register(Avaliacao)