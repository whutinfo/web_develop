# Generated by Django 2.1.5 on 2019-02-20 11:20

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Models', '0039_auto_20190130_1711'),
    ]

    operations = [
        migrations.CreateModel(
            name='Temperature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperate', models.IntegerField(null=True)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'Temperature_Table',
            },
        ),
        migrations.AlterModelOptions(
            name='video',
            options={'managed': False},
        ),
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
