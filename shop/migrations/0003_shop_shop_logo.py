# Generated by Django 4.0.4 on 2022-05-14 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_rename_shop_description_shop_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='shop_logo',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
