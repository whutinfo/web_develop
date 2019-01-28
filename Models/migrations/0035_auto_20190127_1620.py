# Generated by Django 2.1.5 on 2019-01-27 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Models', '0034_auto_20190123_1640'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ip', models.GenericIPAddressField()),
                ('port', models.ImageField(default='80', upload_to='')),
                ('name', models.CharField(max_length=20)),
                ('pwd', models.CharField(max_length=32)),
                ('rtsp_port', models.IntegerField(default='553')),
                ('stream_type', models.IntegerField(default='1')),
            ],
            options={
                'db_table': 'video_conf',
            },
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