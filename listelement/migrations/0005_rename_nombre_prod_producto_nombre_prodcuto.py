# Generated by Django 4.0.4 on 2022-11-06 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listelement', '0004_rename_description_producto_descripcion_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='nombre_prod',
            new_name='nombre_prodcuto',
        ),
    ]
