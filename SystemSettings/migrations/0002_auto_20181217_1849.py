# Generated by Django 2.1.4 on 2018-12-17 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SystemSettings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goodscat',
            old_name='goodsName',
            new_name='goodsCat',
        ),
    ]
