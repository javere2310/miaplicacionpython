from django.shortcuts import render, redirect
from .models import Curso
from django.contrib import messages
from django.core.paginator import Paginator
import requests

# Create your views here.
def inicio(request):
    return render(request, "index.html")

def home(request):

    if request.GET.get('page') is None:
        _page_number = 1
    else:
        _page_number = request.GET.get('page')

    if request.GET.get('filtro') is None:
        _filtro = ''
        cursos = Curso.objects.order_by('nombre').all()
    else:
        _filtro = request.GET.get('filtro')
        cursos = Curso.objects.filter(nombre__icontains=_filtro).order_by('nombre')

    _paginator = Paginator(cursos, 10) # Show 25 contacts per page.
    cursos_page = _paginator.get_page(_page_number)
    return render(request, "gestionCursos.html", {"listacursos": cursos_page, "filtro": _filtro})

def registrarCurso(request):
    _id = int(Curso.objects.latest('codigo').codigo)
    _codigo = str(_id + 1).rjust(6, '0')
    _nombre = request.POST['txtnombre']
    _creditos = request.POST['numcreditos']

    curso = Curso.objects.create(codigo = _codigo, nombre = _nombre, creditos = _creditos)
    messages.success(request, '¡Curso registrado!')
    return redirect('/academico')

def edicionCurso(request, id):
    curso = Curso.objects.get(codigo = id)
    return render(request, "edicionCurso.html", {"curso" : curso})

def eliminarCurso(request, id):
    curso = Curso.objects.get(codigo = id)
    curso.delete()
    messages.success(request, '¡Curso eliminado!')
    return redirect('/academico')

def editarCurso(request):
    _codigo = request.POST['txtcodigo']
    _nombre = request.POST['txtnombre']
    _creditos = request.POST['numcreditos']
    curso = Curso.objects.get(codigo = _codigo)
    curso.nombre = _nombre
    curso.creditos = _creditos
    curso.save()
    messages.success(request, '¡Curso actualizado!')
    return redirect('/academico')

def consulta_cf(request):
    _template = "consultacf.html"

    if request.GET.get('txtCF') is None:
        _txtCF = ''
    else:
        _txtCF = request.GET.get('txtCF')

    if request.GET.get('txtCliente') is None:
        _txtCliente = ''
    else:
        _txtCliente = request.GET.get('txtCliente')

    params = {
        "codigocf":_txtCF,
        "codunico":'',
        "origen":'',
        "producto":'',
        "cliente":_txtCliente,
        "beneficiario":'',
        "fechaemision":'',
    }

    #response = generate_request_post('http://127.0.0.1:5000/CartaFianza/ConsultaCF', params)
    response = generate_request_get('http://127.0.0.1:5000/CartaFianza/ListasGenericas')
    # print(response)
    # if response:
    #    print(response)

    _object = {
        "listacf":[],
        "txtCF": _txtCF,
        "txtCliente": _txtCliente
    }
    return render(request, _template, _object)


def generate_request_get(url, params={}):
    response = requests.get(url, params=params)
    print("response", response)
    if response.status_code == 200:
        print("response", response.json())
        return response.json()
    
def generate_request_post(url, params={}):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("POST", url, headers=headers, data=params)
    print("response", response)
    if response.status_code == 200:
        return response.json()