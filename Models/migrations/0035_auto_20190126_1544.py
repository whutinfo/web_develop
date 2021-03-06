# Generated by Django 2.1.4 on 2019-01-26 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Models', '0034_auto_20190123_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsinfo',
            name='cat',
            field=models.ForeignKey(db_column='catId', null=True, on_delete=django.db.models.deletion.CASCADE, to='Models.GoodsCat'),
        ),
        migrations.AlterField(
            model_name='stockin',
            name='cat',
            field=models.ForeignKey(db_column='catId', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='goodsCat_in', to='Models.GoodsCat'),
        ),
        migrations.AlterField(
            model_name='stockout',
            name='cat',
            field=models.ForeignKey(db_column='catId', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='goodsCat_out', to='Models.GoodsCat'),
        ),
    ]
