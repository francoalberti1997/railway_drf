# Generated by Django 4.2.5 on 2023-12-12 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_railway', '0005_rename_trabajo_experiencia_nombre_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='')),
            ],
        ),
    ]
