# Generated by Django 3.2.3 on 2021-06-06 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0003_auto_20210605_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='imgServicio',
            field=models.ImageField(null=True, upload_to='imgS', verbose_name='Imagen del Servicio'),
        ),
        migrations.AddField(
            model_name='tiposervicio',
            name='imgTipo',
            field=models.ImageField(null=True, upload_to='imgTS', verbose_name='Imagen del Tipo Servicio'),
        ),
    ]
