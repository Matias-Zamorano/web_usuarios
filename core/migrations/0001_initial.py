# Generated by Django 3.2.4 on 2021-07-04 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cursos',
            fields=[
                ('nombre', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Nombre')),
                ('correo', models.CharField(max_length=150, verbose_name='Correo')),
                ('tipo_curso', models.CharField(max_length=50, verbose_name='Tipo_curso')),
            ],
        ),
    ]
