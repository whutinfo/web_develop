# Generated by Django 2.1.4 on 2019-01-13 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Models', '0013_access'),
    ]

    operations = [
        migrations.AlterField(
            model_name='access',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='access',
            name='update_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
