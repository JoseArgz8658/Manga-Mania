# Generated by Django 5.0.6 on 2024-06-25 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BiblioMania', '0009_suscripcion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suscripcion',
            name='precio',
        ),
        migrations.AlterField(
            model_name='suscripcion',
            name='tipo_suscripcion',
            field=models.CharField(choices=[('M', 'Mensual $10 Dolares'), ('A', 'Anual $60 Dolares')], max_length=1),
        ),
    ]
