# Generated by Django 4.0.4 on 2022-05-15 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_shop_shop_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='item',
        ),
        migrations.AddField(
            model_name='inventory',
            name='item',
            field=models.ManyToManyField(blank=True, to='shop.item'),
        ),
    ]