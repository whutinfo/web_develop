# Generated by Django 2.1.4 on 2019-01-19 12:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Models', '0018_seller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='create_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
