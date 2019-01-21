from django.db import models
import django.utils.timezone as timezone
'''
角色是用户的组，角色与用户是多对多

角色里的用户当然拥有该角色的所有权限

但对于角色下的个别用户也需要有特殊权限

结论是不仅角色与用户多对多，用户还需要可以单独进行设置权限，，，，，

做系统就要做够灵活的
'''

class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    node = models.CharField(max_length=32)
    describe = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    permissions = models.ManyToManyField('Menu', through='Role_Menu',through_fields=('role','menu'))
    # through_fields 接收一个二元组 ('field1', 'field2') ，
    # 其中 field1 为指向定义 ManyToManyField 字段的模型的外键名称（本例中为 role）
    # field2 为指向目标模型的外键的名称（本例中为 menu ）
    #ManyToMany的列名一般用复数

    class Meta:
        db_table = 'Role_Table'


#用户表   每个用户都有多个权限
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    pwd = models.CharField(max_length=32)
    create_time = models.DateTimeField(default = timezone.now)
    update_time = models.DateTimeField(auto_now=True)
    zgaccess_str = models.CharField(db_column='ZGaccess_str', max_length=20,null=True)  # Field name made lowercase.
    roles = models.ManyToManyField('Role', through='User_Role',through_fields=('user','role'))
    menus = models.ManyToManyField('Menu', through='User_Menu',through_fields=('user','menu'))
    class Meta:
       # managed = False
        db_table = 'User_Table'

class User_Role(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True) #外键一般用目标模型的小写
    role = models.ForeignKey(Role,on_delete=models.CASCADE,null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'UserRole_Table'

class Menu(models.Model):
    menu_id = models.AutoField(primary_key=True)
    menu_name = models.CharField(max_length=20)
    menu_describe = models.TextField(blank=True, null=True)
    menu_url = models.CharField(max_length=64)
    menu_img = models.CharField(max_length=20)
    menu_show = models.IntegerField(blank=True, null=True)
    menu_open = models.IntegerField(blank=True, null=True)
    menu_node = models.CharField(max_length=64)
    maxchild = models.CharField(max_length=32,null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'Menu_Table'

class Role_Menu(models.Model):
    role = models.ForeignKey(Role,on_delete=models.CASCADE,null=True)
    menu = models.ForeignKey(Menu,on_delete=models.CASCADE,null=True)
    access_str = models.CharField(max_length=20)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'RolePermis_Table'

class User_Menu(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True)
    access_str = models.CharField(max_length=20)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'UserPermis_Table'

class Department(models.Model):
    name = models.CharField(max_length=20)
    node = models.CharField(max_length=32)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    roles = models.ManyToManyField('Role', through='Depart_Role',through_fields=('depart','role'))
    users = models.ManyToManyField('User', through='Depart_User',through_fields=('depart','user'))
    class Meta:
        db_table = 'Department_Table'

class Depart_Role(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)
    depart = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'DepartRole_Table'

#多个部门可能有同一个角色，一个角色对应多个用户
#不能只凭角色找人，不然可能是A部门的也可能是B部门的
class Depart_User(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    depart = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'DepartUser_Table'


#菜单的增删改查打印等权限  只是为了前端显示，目前没有实际用
class Access(models.Model):
    access_name = models.CharField(max_length=20)
    menu_describe = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True,null=True)
    update_time = models.DateTimeField(auto_now=True,null=True)

    class Meta:
        db_table = 'Access_Table'


#供应商
class Supplier(models.Model):
    name = models.TextField(blank=True, null=True)
    managername = models.CharField(db_column='managerName',max_length=10) # Field name made lowercase.
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=64)
    class Meta:
        managed = False
        db_table = 'Supplier_Table'

#商品名称
class Goods(models.Model):

    goodsname = models.CharField(db_column='goodsName', max_length=32)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Goods_Table'

#生产厂家
class Manufactor(models.Model):
    name = models.CharField(max_length=40)
    manager = models.CharField(db_column='managerName',max_length=15)  # Field name made lowercase.
    phone = models.CharField(max_length=50)
    address = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Manufactor_Table'



class GoodsCat(models.Model):
    catname = models.TextField(db_column='catName', blank=True, null=True)  # Field name made lowercase.
    class Meta:
        #managed = False
        db_table = 'goodsCat_Table'


#销售商   wangyu add
class Seller(models.Model):
    name = models.TextField(blank=True, null=True)
    Sellername = models.CharField(db_column='SellerName',max_length=10) # Field name made lowercase.
    Sellerphone = models.CharField(max_length=50) #商户名称
    Sellerproperty = models.CharField(max_length=64)#商户属性
    SellerOwner = models.CharField(max_length=64)  # 负责人姓名
    SellerOwnerPhone = models.CharField(max_length=64)  # 负责人手机号
    SellerOwnerLevel = models.CharField(max_length=64)  # 所属楼栋
    SellerOwnerNo = models.CharField(max_length=64)  # 所属编号
    #models.FloatField()
    SellerOwnerArea = models.CharField(max_length=64)  # 占地面积
    class Meta:
       # managed = False
        db_table = 'Seller_Table'



#商户信息   wangyu add
'''
class Seller(models.Model):
    name = models.TextField(blank=True, null=True)
    Sellername = models.CharField(db_column='SellerName',max_length=10) # Field name made lowercase.
    Sellerphone = models.CharField(max_length=50) #商户名称
    Sellerproperty = models.CharField(max_length=64)#商户属性
    SellerOwner = models.CharField(max_length=64)  # 负责人姓名
    SellerOwnerPhone = models.CharField(max_length=64)  # 负责人手机号
    SellerOwnerLevel = models.CharField(max_length=64)  # 所属楼栋
    SellerOwnerNo = models.CharField(max_length=64)  # 所属编号
    #models.FloatField()
    SellerOwnerArea = models.CharField(max_length=64)  # 占地面积
    class Meta:
        managed = False
        db_table = 'Seller_Table'


'''
#商户属性信息   wangyu add
class SellerPorprety(models.Model):
    #name = models.TextField(blank=True, null=True)
    SellerpropertyType = models.CharField(db_column='SellerP_Str',max_length=10) # Field name made lowercase.
#    SellerpropertyID = models.AutoField(db_column='Inx')
    class Meta:
        #managed = False
        db_table = 'SellerPorprety_Table'

