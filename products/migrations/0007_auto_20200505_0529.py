# Generated by Django 3.0.6 on 2020-05-05 00:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20200505_0522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_image',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='products.Product'),
        ),
        migrations.AlterField(
            model_name='product_variant',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='products.Product'),
        ),
    ]