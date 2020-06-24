# Generated by Django 3.0.6 on 2020-06-17 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_promotionalcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='promotionalcode',
            name='max_uses',
            field=models.IntegerField(default=10, verbose_name='Máximo de usos'),
        ),
        migrations.AddField(
            model_name='promotionalcode',
            name='uses_count',
            field=models.IntegerField(default=0, verbose_name='Veces usado'),
        ),
    ]