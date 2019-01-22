# Generated by Django 2.1.4 on 2019-01-22 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Models', '0025_stockin_stockout'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customermanager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('birthday', models.TextField(blank=True, null=True)),
                ('sex', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('carid', models.TextField(blank=True, db_column='carId', null=True)),
                ('point', models.CharField(max_length=50)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Customermanager',
            },
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
