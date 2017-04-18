from django.shortcuts import render
from django.http import HttpResponse
from models import Pages
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template
from django.template import Context
# Create your views here.

def mostrar(request):
    if request.user.is_authenticated():
        logged = ("Logged in as " + request.user.username +
                 ". <a href='/logout/'>Logout</a><br/><br/>")
    else:
        logged = "Not logged in. <a href='/login/'>Login</a><br/><br/>"

    respuesta = "Pages Found: "
    lista_pages = Pages.objects.all()
    for page in lista_pages:
        respuesta += ("<br>-<a href='/" + page.name + "'>" + page.name +
                 "</a> --> " + page.page)

    plantilla = get_template("plantilla.html")
    contexto = Context({'title': logged, 'content': respuesta})
    return HttpResponse(plantilla.render(contexto))


@csrf_exempt
def mostrar_pagina(request, resource):
    if request.user.is_authenticated():
        login = ("Logged in as " + request.user.username +
                 ". <a href='/logout/'>Logout</a><br/><br/>")
    else:
        login = "Not logged in. <a href='/login/'>Login</a><br/><br/>"

    if request.method == "GET":
        try:
            page = Pages.objects.get(name=resource)
            return HttpResponse(page.page)
        except Pages.DoesNotExist:
            respuesta = "Page not found, add: "
            respuesta += '<form action="" method="POST">'
            respuesta += "Nombre: <input type='text' name='nombre'>"
            respuesta += "<br>Página: <input type='text' name='page'>"
            respuesta += "<input type='submit' value='Enviar'></form>"
    elif request.method == "POST":
        if request.user.is_authenticated():
            nombre = request.POST['nombre']
            page = request.POST['page']
            pagina = Pages(name=nombre, page=page)
            pagina.save()
            respuesta = "Saved page: /" + nombre + " --> " + page
        else:
            respuesta = "Necesitas hacer <a href='/login/'>Login</a>"

    plantilla = get_template("plantilla.html")
    contexto = Context({'title': login, 'content': respuesta})

    return HttpResponse(plantilla.render(contexto))
