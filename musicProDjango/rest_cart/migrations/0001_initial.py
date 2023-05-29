# Generated by Django 4.0.4 on 2023-05-28 04:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0001_initial'),
        ('sessions', '0001_initial'),
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('subtotal', models.IntegerField(default=0, verbose_name='Subtotal')),
                ('total', models.IntegerField(default=0, verbose_name='Total')),
                ('direccion', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.direccion')),
            ],
        ),
        migrations.CreateModel(
            name='CarritoProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=1, verbose_name='Cantidad')),
                ('total', models.IntegerField(default=0, verbose_name='Total')),
                ('carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_cart.carrito')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.producto')),
            ],
        ),
        migrations.AddField(
            model_name='carrito',
            name='productos',
            field=models.ManyToManyField(blank=True, through='rest_cart.CarritoProducto', to='products.producto'),
        ),
        migrations.AddField(
            model_name='carrito',
            name='sesion',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sessions.session'),
        ),
        migrations.AddField(
            model_name='carrito',
            name='tienda',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.tienda'),
        ),
        migrations.AddField(
            model_name='carrito',
            name='usuario',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]