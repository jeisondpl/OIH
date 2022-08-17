# Generated by Django 4.0.6 on 2022-07-14 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lugares',
            fields=[
                ('id', models.AutoField(max_length=20, primary_key=True, serialize=False, unique=True, verbose_name='idCategoria')),
                ('pais', models.CharField(max_length=20, null=True, verbose_name='País')),
                ('departamento', models.CharField(max_length=20, null=True, verbose_name='Departamento')),
                ('ciudad', models.CharField(max_length=20, null=True, verbose_name='Ciudad')),
                ('nombreLugar', models.CharField(max_length=20, null=True, verbose_name='Nombre del lugar')),
            ],
            options={
                'verbose_name': 'Lugar',
                'verbose_name_plural': 'lugares',
            },
        ),
    ]
