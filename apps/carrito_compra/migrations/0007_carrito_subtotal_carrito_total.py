# Generated by Django 4.1.5 on 2023-01-26 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrito_compra', '0006_carrito_cantidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrito',
            name='subtotal',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='carrito',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]
