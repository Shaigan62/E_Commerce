# Generated by Django 3.0.3 on 2020-05-04 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product_Variants',
            new_name='Product_Variant',
        ),
    ]
