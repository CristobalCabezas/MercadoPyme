# Generated by Django 4.0.4 on 2022-11-20 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listelement', '0015_producto_imagen_delete_productoimagenes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio_producto',
            field=models.IntegerField(null=True),
        ),
    ]
