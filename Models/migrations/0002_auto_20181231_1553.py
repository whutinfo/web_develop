# Generated by Django 2.1.4 on 2018-12-31 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Models', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='role_menu',
            old_name='menu_id',
            new_name='menu',
        ),
        migrations.RenameField(
            model_name='role_menu',
            old_name='role_id',
            new_name='role',
        ),
        migrations.RenameField(
            model_name='user_role',
            old_name='role_id',
            new_name='role',
        ),
        migrations.RenameField(
            model_name='user_role',
            old_name='user_id',
            new_name='user',
        ),
    ]