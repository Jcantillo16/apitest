# Generated by Django 4.1.5 on 2023-01-26 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrito_compra', '0008_carrito_descuento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrito',
            name='descuento',
            field=models.FloatField(default=0),
        ),
    ]