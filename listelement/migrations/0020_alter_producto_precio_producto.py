# Generated by Django 4.0.4 on 2022-11-21 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listelement', '0019_alter_producto_precio_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio_producto',
            field=models.IntegerField(null=True),
        ),
    ]
