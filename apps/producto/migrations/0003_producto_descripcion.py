# Generated by Django 4.1.5 on 2023-01-24 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0002_producto_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
