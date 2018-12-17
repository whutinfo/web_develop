from django.db import models


class Goods(models.Model):
    goodsName=models.CharField(max_length=32)


class GoodsCat(models.Model):
    goodsCat=models.CharField(max_length=32)

class Manufactor(models.Model):
    name=models.CharField(max_length=32)
    manager=models.CharField(max_length=32)
    phone=models.CharField(max_length=32)
    address=models.CharField(max_length=32)
