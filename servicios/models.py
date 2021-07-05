from django.db import models


class TipoServicio(models.Model):
    idTipo = models.IntegerField(primary_key=True, verbose_name='Id Tipo Servicio')
    nombreTipo = models.CharField(max_length=50, verbose_name='Nombre Tipo Servicio')
    imgTipo = models.ImageField(upload_to='IMGTS',null= True,verbose_name='Imagen del Tipo Servicio')

    def __str__(self):
        return self.nombreTipo


class Servicio(models.Model):
    idServicio = models.IntegerField(primary_key=True, verbose_name='Id Servicio')
    nombreServicio = models.CharField(max_length=50, verbose_name='Nombre Servicio')
    descrpcion = models.CharField(max_length=400,verbose_name='Descripcion Servicio')
    imgServicio = models.ImageField(upload_to='IMGS',null= True,verbose_name='Imagen del Servicio')
    TipoServicio = models.ForeignKey(TipoServicio, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreServicio





