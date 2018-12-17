from django.db import models


# 必须继承models.Model
class UserInfo(models.Model):
    """
    用户信息表
    """
    # 如果没有写这句，还是会给创建一个名为Id的自增长的主键的一列
    nid=models.AutoField(primary_key=True)#自增长字段，Int型，设为主键

    name=models.CharField(max_length=32)
    password=models.CharField(max_length=64)

    # 在已经创建表的情况多加一列，要么让它允许为空，要么给个默认值  如下
    age=models.IntegerField(null=True)
    # age=models.IntegerField(default=1)

    # on_delete这个参数必须写，一般情况下使用CASCADE就可以了，级联删除
    #在数据库中创建的列名为ug_id
    ug=models.ForeignKey('UserGroup',on_delete=models.CASCADE,null=True)
    ut=models.ForeignKey('UserType',on_delete=models.CASCADE,null=True)

class UserType(models.Model):
    """
    用户类型
    """
    title = models.CharField(max_length=32)

class UserGroup(models.Model):
    title = models.CharField(max_length=32)
