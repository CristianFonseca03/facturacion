# Generated by Django 2.1.7 on 2019-03-25 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturas', '0002_producto_cantidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='correo',
            field=models.EmailField(default='cristian.lfs@gmail.com', max_length=70, verbose_name='correo'),
            preserve_default=False,
        ),
    ]
