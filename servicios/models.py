from django.db import models


class Tipo_Asesoria(models.Model):
    idTipo = models.IntegerField(primary_key=True, verbose_name='Id Tipo Asesoria')
    nombreTipo = models.CharField(max_length=50, verbose_name='Nombre Tipo Asesoria')

    def __str__(self):
        return self.nombreTipo

class Asesoria(models.Model):
    idAsesoria = models.IntegerField(primary_key=True,verbose_name='Id de asesoria')
    nombreAsesoria = models.CharField(max_length=50,verbose_name='Nombre de la asesoria')
    descrpcion = models.CharField(max_length=400,verbose_name='Descripcion Asesoria')
    Tipo_Asesoria = models.ForeignKey(Tipo_Asesoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreCategoria

class Capacitacion(models.Model):
    idCapacitacion = models.IntegerField(primary_key=True,verbose_name='Id Capacitacion')
    nombreCapa = models.CharField(max_length=50, verbose_name='Nombre Capacitacion')
    descripcion = models.CharField(max_length=400,verbose_name='Descripcion Capacitacion')

    def __str__(self):
        return self.nombreCapa

class Cliente(models.Model):
    rut = models.CharField(primary_key=True,max_length=10, verbose_name='Rut Cliente')
    nombreCli = models.CharField(max_length=100,verbose_name='Nombre Cliente')
    apellidoCli = models.CharField(max_length=100,verbose_name='Apellido Cliente')
    correoCli = models.CharField(max_length=150, verbose_name='Correo Cliente')

    def __str__(self):
        return self.nombreCli
