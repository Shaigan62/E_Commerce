# Generated by Django 3.0.6 on 2020-08-11 14:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('recommenderSystem', '0005_auto_20200811_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_activity',
            name='activity_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]