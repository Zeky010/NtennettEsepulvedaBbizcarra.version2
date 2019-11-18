# Generated by Django 2.2.6 on 2019-11-18 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_pelicula_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pelicula',
            name='imagen',
        ),
        migrations.AddField(
            model_name='autor',
            name='apellido_author',
            field=models.CharField(default='rowling', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='autor',
            name='descripcion_autor',
            field=models.TextField(default='Es un autor genial', help_text='Ingrese informacion del Autor', max_length=1000),
            preserve_default=False,
        ),
    ]
