# Generated by Django 4.2.5 on 2023-12-17 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_railway', '0007_alter_skills_descripcion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('mail', models.CharField(max_length=50)),
                ('celular', models.CharField(max_length=50)),
                ('mensaje', models.CharField(max_length=650)),
            ],
        ),
    ]
