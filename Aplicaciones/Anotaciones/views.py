from django.shortcuts import render

# Create your views here.
def home_anotaciones(request):
    return render(request, "index.html", {"deshabilitado": False, "textoboton": "Probar"})