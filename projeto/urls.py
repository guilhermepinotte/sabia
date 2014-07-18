from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'projeto.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^sabia/', include('sabia.urls', namespace="sabia")),
    url(r'^admin/', include(admin.site.urls)),
)
