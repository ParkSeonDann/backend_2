# Generated by Django 5.1.1 on 2024-11-09 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0021_merge_20241108_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subasta',
            name='estado',
            field=models.CharField(choices=[('vigente', 'Vigente'), ('pendiente', 'Pendiente'), ('cerrada', 'Cerrada')], default='vigente', max_length=20),
        ),
        migrations.AlterField(
            model_name='transaccion',
            name='estado',
            field=models.CharField(max_length=20),
        ),
    ]
