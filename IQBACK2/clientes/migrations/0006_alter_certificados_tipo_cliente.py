# Generated by Django 4.1.7 on 2023-05-17 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0005_certificados_formularios_saq'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificados',
            name='tipo_cliente',
            field=models.CharField(max_length=16),
        ),
    ]
