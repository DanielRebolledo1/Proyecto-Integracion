# Generated by Django 4.0.4 on 2022-05-11 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id del producto')),
                ('nombreProducto', models.CharField(max_length=75, verbose_name='Nombre del producto')),
            ],
        ),
    ]
