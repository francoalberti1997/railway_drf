# Generated by Django 4.2.5 on 2023-12-11 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_railway', '0003_experiencia_puesto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proyecto', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='')),
                ('motivacion', models.CharField(max_length=200)),
                ('estado', models.CharField(max_length=25)),
            ],
        ),
    ]
