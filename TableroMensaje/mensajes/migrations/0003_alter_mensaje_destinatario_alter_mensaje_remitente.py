# Generated by Django 5.1.1 on 2024-09-09 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mensajes', '0002_rename_creado_en_mensaje_fecha_envio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensaje',
            name='destinatario',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='mensaje',
            name='remitente',
            field=models.CharField(max_length=100),
        ),
    ]
