# Generated by Django 2.1.4 on 2019-01-22 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Models', '0029_auto_20190122_1441'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_sn', models.CharField(db_column='goodsSn', max_length=100)),
                ('goods_stock', models.IntegerField(db_column='goodsStock', null=True)),
                ('sale_count', models.IntegerField(db_column='saleCount', null=True)),
                ('cost', models.FloatField(null=True)),
                ('price', models.FloatField(null=True)),
                ('exp_date', models.DateTimeField(null=True)),
                ('out_time', models.DateTimeField(null=True)),
                ('value3', models.TextField(blank=True, null=True)),
                ('value4', models.TextField(blank=True, null=True)),
                ('cat', models.ForeignKey(db_column='catId', null=True, on_delete=django.db.models.deletion.CASCADE, to='Models.GoodsCat')),
                ('goods', models.ForeignKey(db_column='goodsId', null=True, on_delete=django.db.models.deletion.CASCADE, to='Models.Goods')),
                ('manufactor', models.ForeignKey(db_column='manufactorId', null=True, on_delete=django.db.models.deletion.CASCADE, to='Models.Manufactor')),
                ('seller', models.ForeignKey(db_column='sellerId', null=True, on_delete=django.db.models.deletion.CASCADE, to='Models.Seller')),
            ],
            options={
                'db_table': 'GoodsInfo_Table',
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
        migrations.AddField(
            model_name='goodsinfo',
            name='stockin',
            field=models.ForeignKey(db_column='stockIn_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='Models.StockIn'),
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='supplier',
            field=models.ForeignKey(db_column='supplierId', null=True, on_delete=django.db.models.deletion.CASCADE, to='Models.Supplier'),
        ),
    ]
