from django.shortcuts import render
from django.shortcuts import HttpResponse
from Models import models
import json
from Base.com_func import *

def goods(request):
    action = request.POST.get('action')
    '''sys code define variable begin  '''
    column = ''
    '''sys code define variable begin  '''

    if request.method == 'GET':
        '''user code define variable begin  '''

        databasename = 'aliyun'
        tablename = 'Goods_Table'  #在数据库找到想要获取字段的表，应为数据库中真实表名，即Models中的db_table
        ''' id(数据库中自增长的那个字段，同样应为真实字段名)一定要有！！并放在第一个，不是用来显示，用来处理信息  其余顺序根据前端想要的摆放顺序来'''
        columnname = ['id', 'goodsName']   #  在数据库找到想要获取的字段，应为数据库中真实的字段名,即Models中的db_column，如有的话
        columncnt = 2       #需要获取的列的数量 包括id
        columnwidth = [0, 18]       #列的宽度 个数与cnt匹配
        columnalign = ['center']*columncnt  #对齐格式 个数与cnt匹配

        '''user code define variable  end  '''

        '''sys code begin  '''
        column = fun_Get_Cmd_Trans(databasename, tablename, columnname, columncnt, columnwidth, columnalign)
        '''sys code end'''

        '''usr code begin  '''
        return render(request, 'SystemSettings/goods.html', {'info_dict': column})
        '''usr code end '''

    else:
        '''user code define variable begin  '''
        model_name = models.Goods  # 想要展示的表的Model对象
        '''user code define variable end  '''

        '''usr code begin  '''

        if action=='LoadData':
            querys=model_name.objects.all() #获取需要的字段名的数据
            value_dict = {'value0':'','value1':''}
            value_list = []
            for row in querys:
                value_dict['value0'] = row.id #一定要获取id 并放进第一个value0
                value_dict['value1']=row.goodsname  # 根据前端想要的摆放顺序来
                value_list.append(value_dict.copy())  #直接使用append方法将字典添加到列表中，如果需要更改字典中的数据，那么列表中的内容也会发生改变
                #用.copy()就不会跟着改变
                value_dict.clear()  # 防止出错时保存了上一次的值而导致看不出问题在哪

            return HttpResponse(json.dumps(value_list))#将列表拼字典仿Json格式转字符串传给前端 [{},{},{}]
        elif action=='Save':
            back = 0
            add_goods=request.POST.get('name')
            models.Goods.objects.create(goodsname=add_goods)
            back = 1
            return HttpResponse(back)

        '''usr code end '''

def goodsCat(request):
    action = request.POST.get('action')

    '''sys code define variable begin  '''
    column = ''
    '''sys code define variable begin  '''

    if request.method == 'GET':
        '''user code define variable begin  '''

        databasename = 'aliyun'
        tablename = 'goodsCat_Table'  # 在数据库找到想要获取字段的表，应为数据库中真实表名，即Models中的db_table
        ''' id(数据库中自增长的那个字段，同样应为真实字段名)一定要有！！并放在第一个，不是用来显示，用来处理信息  其余顺序根据前端想要的摆放顺序来'''
        columnname = ['id', 'catName']  # 在数据库找到想要获取的字段，应为数据库中真实的字段名,即Models中的db_column，如有的话
        columncnt = 2  # 需要获取的列的数量 包括id
        columnwidth = [0, 18]  # 列的宽度 个数与cnt匹配
        columnalign = ['center'] * columncnt  # 对齐格式 个数与cnt匹配   可以不用改！！

        '''user code define variable  end  '''

        '''sys code begin  '''
        column = fun_Get_Cmd_Trans(databasename, tablename, columnname, columncnt, columnwidth, columnalign)
        '''sys code end'''

        '''usr code begin  '''
        return render(request, 'SystemSettings/goodsCat.html', {'info_dict': column})
        '''usr code end '''

    else:
        '''user code define variable begin  '''
        model_name = models.GoodsCat  # 想要展示的表的Model对象
        '''user code define variable end  '''

        '''usr code begin  '''

        if action == 'LoadData':
            querys = model_name.objects.all()  # 获取需要的字段名的数据
            value_dict = {'value0': '', 'value1': ''}  # 有几个需要的列就有多少value 包括Id
            value_list = []
            for row in querys:
                value_dict['value0'] = row.id  # 一定要获取id 并放进第一个value0
                value_dict['value1'] = row.catname  # 根据前端想要的摆放顺序来

                value_list.append(value_dict.copy())  # 直接使用append方法将字典添加到列表中，如果需要更改字典中的数据，那么列表中的内容也会发生改变
                # 用.copy()就不会跟着改变
                value_dict.clear()  # 防止出错时保存了上一次的值而导致看不出问题在哪

            return HttpResponse(json.dumps(value_list))  # 将列表拼字典仿Json格式转字符串传给前端 [{},{},{}]
        elif action == 'Save':
            back = 0
            add_goodsCat = request.POST.get('name')
            back = 1
            models.GoodsCat.objects.create(catname=add_goodsCat)
            return HttpResponse(back)

        '''usr code end '''


def manufactor(request):
    action = request.POST.get('action')

    '''sys code define variable begin  '''
    column = ''
    '''sys code define variable begin  '''

    if request.method == 'GET':
        '''user code define variable begin  '''

        databasename = 'aliyun'
        tablename = 'Manufactor_Table'  # 在数据库找到想要获取字段的表，应为数据库中真实表名，即Models中的db_table
        ''' id(数据库中自增长的那个字段，同样应为真实字段名)一定要有！！并放在第一个，不是用来显示，用来处理信息  其余顺序根据前端想要的摆放顺序来'''
        columnname = ['id', 'name', 'managerName', 'phone',
                      'address']  # 在数据库找到想要获取的字段，应为数据库中真实的字段名,即Models中的db_column，如有的话
        columncnt = 5  # 需要获取的列的数量 包括id
        columnwidth = [0, 18, 10, 12, 20]  # 列的宽度 个数与cnt匹配
        columnalign = ['center'] * columncnt  # 对齐格式 个数与cnt匹配   可以不用改！！

        '''user code define variable  end  '''

        '''sys code begin  '''
        column = fun_Get_Cmd_Trans(databasename, tablename, columnname, columncnt, columnwidth, columnalign)
        '''sys code end'''

        '''usr code begin  '''
        return render(request, 'SystemSettings/manufactor.html', {'info_dict': column})
        '''usr code end '''

    else:
        '''user code define variable begin  '''
        model_name = models.Manufactor  # 想要展示的表的Model对象
        '''user code define variable end  '''

        '''usr code begin  '''

        if action == 'LoadData':
            querys = model_name.objects.all()  # 获取需要的字段名的数据
            value_dict = {'value0': '', 'value1': '', 'value2': '', 'value3': '', 'value4': ''}  # 有几个需要的列就有多少value 包括Id
            value_list = []
            for row in querys:
                value_dict['value0'] = row.id  # 一定要获取id 并放进第一个value0
                value_dict['value1'] = row.name  # 根据前端想要的摆放顺序来
                value_dict['value2'] = row.manager  # 负责人姓名
                value_dict['value3'] = row.phone  # 负责人联系电话
                value_dict['value4'] = row.address  # 生产厂商地址
                value_list.append(value_dict.copy())  # 直接使用append方法将字典添加到列表中，如果需要更改字典中的数据，那么列表中的内容也会发生改变
                # 用.copy()就不会跟着改变
                value_dict.clear()  # 防止出错时保存了上一次的值而导致看不出问题在哪

            return HttpResponse(json.dumps(value_list))  # 将列表拼字典仿Json格式转字符串传给前端 [{},{},{}]
        elif action == 'Save':
            back = 0
            add_goods = request.POST.get('name')
            models.Goods.objects.create(goodsname=add_goods)
            back = 1
            return HttpResponse(back)

        '''usr code end '''


def supplier(request):
    action = request.POST.get('action')

    '''sys code define variable begin  '''
    column = ''
    '''sys code define variable begin  '''

    if request.method == 'GET':
        '''user code define variable begin  '''

        databasename = 'aliyun'
        tablename = 'Supplier_Table'  # 在数据库找到想要获取字段的表，应为数据库中真实表名，即Models中的db_table
        ''' id(数据库中自增长的那个字段，同样应为真实字段名)一定要有！！并放在第一个，不是用来显示，用来处理信息  其余顺序根据前端想要的摆放顺序来'''
        columnname = ['id', 'name', 'managerName', 'phone',
                      'address']  # 在数据库找到想要获取的字段，应为数据库中真实的字段名,即Models中的db_column，如有的话
        columncnt = 5  # 需要获取的列的数量 包括id
        columnwidth = [0, 18, 10, 12, 20]  # 列的宽度 个数与cnt匹配
        columnalign = ['center'] * columncnt  # 对齐格式 个数与cnt匹配   可以不用改！！

        '''user code define variable  end  '''

        '''sys code begin  '''
        column = fun_Get_Cmd_Trans(databasename, tablename, columnname, columncnt, columnwidth, columnalign)
        '''sys code end'''

        '''usr code begin  '''
        return render(request, 'SystemSettings/supplier.html', {'info_dict': column})
        '''usr code end '''

    else:
        '''user code define variable begin  '''
        model_name = models.Supplier  # 想要展示的表的Model对象
        '''user code define variable end  '''

        '''usr code begin  '''

        if action == 'LoadData':
            querys = model_name.objects.all()  # 获取需要的字段名的数据
            value_dict = {'value0': '', 'value1': '', 'value2': '', 'value3': '', 'value4': ''}  # 有几个需要的列就有多少value 包括Id
            value_list = []
            for row in querys:
                value_dict['value0'] = row.id  # 一定要获取id 并放进第一个value0
                value_dict['value1'] = row.name  # 根据前端想要的摆放顺序来
                value_dict['value2'] = row.managername  # 负责人姓名
                value_dict['value3'] = row.phone  # 负责人联系电话
                value_dict['value4'] = row.address  # 生产厂商地址
                value_list.append(value_dict.copy())  # 直接使用append方法将字典添加到列表中，如果需要更改字典中的数据，那么列表中的内容也会发生改变
                # 用.copy()就不会跟着改变
                value_dict.clear()  # 防止出错时保存了上一次的值而导致看不出问题在哪

            return HttpResponse(json.dumps(value_list))  # 将列表拼字典仿Json格式转字符串传给前端 [{},{},{}]
        elif action == 'Save':
            back = 0
            add_name = request.POST.get('name')
            add_manager=request.POST.get('manager')
            add_phone=request.POST.get('phone')
            add_address=request.POST.get('address')
            models.Supplier.objects.create(name=add_name,phone=add_phone,managername=add_manager,address=add_address)
            back = 1
            return HttpResponse(back)
        '''usr code end '''


#售卖页面  销售页面的处理函数
def Seller_Trans(request):
    action = request.POST.get('action')

    '''sys code define variable begin  '''
    column = ''
    '''sys code define variable begin  '''

    if request.method == 'GET':
        '''user code define variable begin  '''

        databasename = 'aliyun'
        tablename = 'Seller_Table'  # 在数据库找到想要获取字段的表，应为数据库中真实表名，即Models中的db_table
        ''' id(数据库中自增长的那个字段，同样应为真实字段名)一定要有！！并放在第一个，不是用来显示，用来处理信息  其余顺序根据前端想要的摆放顺序来'''
        columnname = ['id', 'SellerName', 'Sellerproperty', 'SellerOwner','SellerOwnerPhone', 'SellerOwnerLevel',
                      'SellerOwnerNo','SellerOwnerArea']  # 在数据库找到想要获取的字段，应为数据库中真实的字段名,即Models中的db_column，如有的话
        columncnt = 8  # 需要获取的列的数量 包括id
        columnwidth = [0, 18, 15, 12, 12, 12, 12, 20]  # 列的宽度 个数与cnt匹配  第一个对应的Id,id 不显示，赋0即可
        columnalign = ['center'] * columncnt  # 对齐格式 个数与cnt匹配   可以不用改！！

        '''user code define variable  end  '''

        '''sys code begin  '''
        column = fun_Get_Cmd_Trans(databasename, tablename, columnname, columncnt, columnwidth, columnalign)
        '''sys code end'''

        '''usr code begin  '''
        return render(request, 'SystemSettings/Seller.html', {'info_dict': column})
        '''usr code end '''

    else:
        '''user code define variable begin  '''
        model_name = models.Seller  # 想要展示的表的Model对象
        '''user code define variable end  '''

        '''usr code begin  '''

        if action == 'LoadData':
            querys = model_name.objects.all()  # 获取需要的字段名的数据
            value_dict = {'value0': '', 'value1': '', 'value2': '', 'value3': '', 'value4': '', 'value5': '', 'value6': '', 'value7': ''}  # 有几个需要的列就有多少value 包括Id
            value_list = []
            for row in querys:
                value_dict['value0'] = row.id  # 一定要获取id 并放进第一个value0
                value_dict['value1'] = row.Sellername  # 根据前端想要的摆放顺序来
                value_dict['value2'] = row.Sellerproperty  # 商户属性
                value_dict['value3'] = row.SellerOwner  # 负责人姓名
                value_dict['value4'] = row.SellerOwnerPhone  # 负责人手机号
                value_dict['value5'] = row.SellerOwnerLevel  # 所属楼栋
                value_dict['value6'] = row.SellerOwnerNo  # 所属编号
                value_dict['value7'] = row.SellerOwnerArea  # 占地面积
                value_list.append(value_dict.copy())  # 直接使用append方法将字典添加到列表中，如果需要更改字典中的数据，那么列表中的内容也会发生改变
                # 用.copy()就不会跟着改变
                value_dict.clear()#防止出错时保存了上一次的值而导致看不出问题在哪

            return HttpResponse(json.dumps(value_list))  # 将列表拼字典仿Json格式转字符串传给前端 [{},{},{}]

        elif action == 'Save':
            back = 0
            add_Sellername = request.POST.get('name')
            add_Sellerproperty = request.POST.get('type')
            add_SellerOwner = request.POST.get('manager')

            add_SellerOwnerPhone = request.POST.get('phone')#request.POST.get('SellerOwnerPhone')
            add_SellerOwnerLevel = request.POST.get('floor')
            add_SellerOwnerNo = request.POST.get('number')
            add_SellerOwnerArea = request.POST.get('area')

            models.Seller.objects.create(Sellername=add_Sellername, Sellerproperty=add_Sellerproperty,SellerOwner=add_SellerOwner,SellerOwnerPhone=add_SellerOwnerPhone,
                                           SellerOwnerLevel = add_SellerOwnerLevel,SellerOwnerNo = add_SellerOwnerNo,SellerOwnerArea = add_SellerOwnerArea )
            back = 1
            return HttpResponse(back)

        elif action == 'LoadSellerPro':
            value_dict = {'type':'','title':''}
            value_list = []
            sellerPros = models.SellerPorprety.objects.all()
            for row in sellerPros:
                value_dict['id'] = row.id
                value_dict['name'] = row.SellerpropertyType
                value_list.append(value_dict.copy())
            return HttpResponse(json.dumps(value_list))
        '''usr code end '''


#销售商的属性配置
def SellerProp_Trans(request):
    action = request.POST.get('action')

    '''sys code define variable begin  '''
    column = ''
    '''sys code define variable begin  '''

    if request.method == 'GET':
        '''user code define variable begin  '''

        databasename = 'aliyun'
        tablename = 'SellerPorprety_Table'  # 在数据库找到想要获取字段的表，应为数据库中真实表名，即Models中的db_table
        ''' id(数据库中自增长的那个字段，同样应为真实字段名)一定要有！！并放在第一个，不是用来显示，用来处理信息  其余顺序根据前端想要的摆放顺序来'''
        columnname = ['id', 'SellerP_Str']  # 在数据库找到想要获取的字段，应为数据库中真实的字段名,即Models中的db_column，如有的话
        columncnt = 2  # 需要获取的列的数量 包括id
        columnwidth = [0, 18]  # 列的宽度 个数与cnt匹配  第一个对应的Id,id 不显示，赋0即可
        columnalign = ['center'] * columncnt  # 对齐格式 个数与cnt匹配   可以不用改！！

        '''user code define variable  end  '''

        '''sys code begin  '''
        column = fun_Get_Cmd_Trans(databasename, tablename, columnname, columncnt, columnwidth, columnalign)
        '''sys code end'''

        '''usr code begin  '''
        return render(request, 'SystemSettings/SellerProperty.html', {'info_dict': column})
        '''usr code end '''

    else:
        '''user code define variable begin  '''
        model_name = models.SellerPorprety  # 想要展示的表的Model对象
        '''user code define variable end  '''

        '''usr code begin  '''

        if action == 'LoadData':
            querys = model_name.objects.all()  # 获取需要的字段名的数据
            value_dict = {'value0': '', 'value1': ''}  # 有几个需要的列就有多少value 包括Id
            value_list = []
            for row in querys:
                value_dict['value0'] = row.id  # 一定要获取id 并放进第一个value0
                value_dict['value1'] = row.SellerpropertyType  # 根据前端想要的摆放顺序来
                value_list.append(value_dict.copy())  # 直接使用append方法将字典添加到列表中，如果需要更改字典中的数据，那么列表中的内容也会发生改变
                # 用.copy()就不会跟着改变
                value_dict.clear()  # 防止出错时保存了上一次的值而导致看不出问题在哪
            return HttpResponse(json.dumps(value_list))  # 将列表拼字典仿Json格式转字符串传给前端 [{},{},{}]

        elif action == 'Save':
            add_Propretyname = request.POST.get('Proprety')
            models.SellerPorprety.objects.create(SellerpropertyType=add_Propretyname)
            return HttpResponse(1)
        elif action == 'LoadSellerPro':
            pass #暂不处理
        '''usr code end '''


