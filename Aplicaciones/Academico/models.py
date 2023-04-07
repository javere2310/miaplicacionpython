from django.db import models

# Create your models here.
class Curso(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)
    creditos = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        text = "{0} ({1} crédito(s))"
        return text.format(self.nombre, self.creditos)
    
class Ciclo(models.Model):
    codigo = models.AutoField(primary_key=True)
    anio = models.PositiveIntegerField()
    nroCiclo = models.PositiveIntegerField()
    activo = models.BooleanField(default=True)

    def __str__(self) -> str:
        txt = "Semestre {0}, Ciclo {1} ({2})"
        if self.activo:
            estado = "Activo"
        else:
            estado = "Inactivo"
        return txt.format(self.anio, self.nroCiclo, estado)