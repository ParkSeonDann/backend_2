# Generated by Django 5.1.1 on 2024-11-07 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0012_alter_usuario_rol'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='comuna',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='region',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]