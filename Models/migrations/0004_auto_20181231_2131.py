# Generated by Django 2.1.4 on 2018-12-31 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Models', '0003_auto_20181231_1603'),
    ]

    operations = [
        migrations.RenameField(
            model_name='role',
            old_name='permission',
            new_name='permissions',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='menu',
            new_name='menus',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='role',
            new_name='roles',
        ),
    ]
