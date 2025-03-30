from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render
"""
def saludo (request):
    #"C:/Users/WELCOME/dj/techno/techno/plantilla/index.html"

    hora=datetime.datetime.now()

    doc_ext=loader.get_template('index.html')

    documento= doc_ext.render({"esta_aludando":hora})
    
    return HttpResponse(documento)
    """
def saludo(request):
    return render (request,'index.html' )
def saludo (request):
    #"C:/Users/WELCOME/dj/techno/techno/plantilla/index.html"

    hora=datetime.datetime.now()

    

    
    return render(request,'index.html',{"esta_aludando":hora})

def despedida (request):
    return HttpResponse("Bueno chau")

def fechita(request):
    fechaAc=datetime.datetime.now()
    
    documento="""<html>
    <body>
    <h1>
    fecha hora actual: %s
    </h1>
    </body>
    </html>"""% fechaAc
    return HttpResponse(documento)

def inicio(request):
    return render (request,'inicio.html' )

def productos(request):
    return render (request,'productos.html' )
