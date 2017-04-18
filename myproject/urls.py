from django.conf.urls import patterns, include, url
from django.contrib import admin
from cms_users_put import views
from django.contrib.auth.views import logout, login

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.mostrar, name= "Lo que hay guardado"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logout/', logout),
    url(r'^login/', login),
    url(r'(.+)', views.mostrar_pagina, name="Vamos o añadimos la pagina"),
)
