# Generated by Django 4.1.5 on 2023-01-26 04:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carrito_compra', '0002_alter_carrito_producto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrito',
            name='cantidad',
        ),
    ]
