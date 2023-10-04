# Generated by Django 4.1.7 on 2023-04-28 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('basedata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='clientes',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('razon_social', models.CharField(max_length=150)),
                ('identificacion', models.CharField(max_length=15)),
                ('nombre_comercial', models.CharField(max_length=150)),
                ('direccion', models.CharField(max_length=150)),
                ('telefono', models.CharField(max_length=15)),
                ('telefono2', models.CharField(default=None, max_length=15, null=True)),
                ('codigo_postal', models.CharField(max_length=150)),
                ('tipo_cliente', models.CharField(max_length=15)),
                ('nivel', models.CharField(max_length=1)),
                ('estado_cliente', models.CharField(max_length=15)),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basedata.ciudades')),
            ],
        ),
        migrations.CreateModel(
            name='contactos',
            fields=[
                ('id_contacto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_contacto', models.CharField(max_length=100, verbose_name='nombre_contacto')),
                ('cargo_contacto', models.CharField(max_length=50, verbose_name='cargo_contacto')),
                ('email_contacto', models.CharField(max_length=100, verbose_name='email_contacto')),
                ('estado_contacto', models.CharField(max_length=15)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.clientes')),
            ],
        ),
        migrations.CreateModel(
            name='certificados',
            fields=[
                ('id_certificado', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_emision', models.DateField()),
                ('fecha_vencimiento', models.DateField()),
                ('tipo_cliente', models.CharField(max_length=15)),
                ('nivel', models.CharField(max_length=1)),
                ('codigo_certificado', models.CharField(max_length=15)),
                ('estado_certificado', models.CharField(max_length=15)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.clientes')),
                ('versiones_norma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basedata.versiones_norma')),
            ],
        ),
    ]