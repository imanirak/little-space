# Generated by Django 4.0.4 on 2022-05-16 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_alter_item_item_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_type',
            field=models.CharField(choices=[('W', 'Women'), ('M', 'Men'), ('Kids', 'Kids'), ('Home', 'Home'), ('Vintage & Collectible', 'Vintage & Collectible '), ('Beauty', 'Beauty'), ('Electronics', 'Electronics'), ('Sports & Outdoors', 'Sports & Outdoors'), ('Handmade', 'Handmade'), ('Other', 'Other')], max_length=150),
        ),
    ]
