# Generated by Django 3.2.3 on 2021-06-06 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0004_auto_20210606_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='imgServicio',
            field=models.ImageField(null=True, upload_to='', verbose_name='Imagen del Servicio'),
        ),
        migrations.AlterField(
            model_name='tiposervicio',
            name='imgTipo',
            field=models.ImageField(null=True, upload_to='', verbose_name='Imagen del Tipo Servicio'),
        ),
    ]