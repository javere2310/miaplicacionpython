from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio),
    path('academico/', views.home),
    path('academico/registrarCurso/', views.registrarCurso),
    path('academico/edicionCurso/<id>', views.edicionCurso),
    path('academico/eliminacionCurso/<id>', views.eliminarCurso),
    path('academico/editarCurso/', views.editarCurso),
    path('academico/consultacf/', views.consulta_cf),
]