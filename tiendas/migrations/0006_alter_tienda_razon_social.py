# Generated by Django 5.1.1 on 2024-10-15 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiendas', '0005_alter_tienda_tienda_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tienda',
            name='razon_social',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]