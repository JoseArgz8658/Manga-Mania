# Generated by Django 5.0.6 on 2024-06-28 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BiblioMania', '0012_alter_suscripcion_suscription_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resena',
            name='user',
        ),
        migrations.DeleteModel(
            name='EstadoMangaUsuario',
        ),
    ]
