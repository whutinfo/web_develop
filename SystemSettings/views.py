from django.shortcuts import render
from django.shortcuts import HttpResponse

from django.db import dbTrans
from Models import models
import json
from Base.views import get_checkbox,get_columns


'''
拼接前端表格的column数据
'''
def json_frame_construct(*var):# <class 'tuple'>: ([4, '生产厂商名称', '负责人姓名', '负责人手机号', '联系地址'],)
    #var = []
    column = []
    var_list = var[0] #该元组只有一组数组
    cnt = var_list[0] #参数个数
    json_frame = {}
    for i in range(1,len(var_list)):
        title = var_list[i]
        width = 18  #这个地方因为for循环导致每一次被固定18了
        width = str(width) + "%"
        align = 'center' #同width
        value = 'value'+str(i)
        json_frame={'field': value, 'title': title, 'width':width, 'align': align}
        column.append(json_frame.copy())
    # [
    #     {'field': 'value1', 'title': '生产厂商名称', 'width': '18%', 'align': 'center'},
    #     {'field': 'value2', 'title': '负责人姓名', 'width': '10%', 'align': 'center'},
    #     {'field': 'value3', 'title': '负责人手机号', 'width': "12%", 'align': 'center'},
    #     {'field': 'value4', 'title': '联系地址', 'width': "20%", 'align': 'center'}]

    #construct json
    return column


'''
base_fun_get_demo : 实现对某个表中的特定字段，将其注释内容返回  即中文列名
形参：table  是特定表的字段
返回值：字段的注释内容，返回类型为字符串类型
'''
def base_fun_get_demo(table):  # table= models.GoodsCat
  #  return str.demo  # 字段的注释
    #目前还不会返回字段注释
    return table.name,table.manager,table.phone,table.address


'''
 针对页面的get命令进行处理
 '''
def get_4_column():
    # 列的数量
    columcnt = 4
    # 列的名字
    comment = []
    model_name = models.Manufactor
    '''目前做不了直接获取这个表对象的所有列名  没有用base_fun_get_demo'''
    #for i in range(columcnt):
       # comment[i] = base_fun_get_demo(model_name)
    comment.append(columcnt)
    comment.append('生产厂商名称')
    comment.append('负责人姓名')
    comment.append('负责人手机号')
    comment.append('联系地址')
    #<class 'list'>: [4,'生产厂商名称', '负责人姓名', '负责人手机号', '联系地址']
    # 构建列的HTML命令
    # comment + head_pre ......
    j_str = json_frame_construct(comment)
    # 获得json数据
    return j_str


def goods(request):
    goods=[]
    action = request.POST.get('action')
    if request.method=='GET':
        return render(request,'SystemSettings/goods.html')
    else:
        if action=='Load':
            goods_list=models.Goods.objects.all()
            value={'value1':''}  #用字典和列表拼接很方便形成Json格式
            for row in goods_list:
                value['value1']=row.goodsname  # [{},{},{}]
                goods.append(value.copy())  #直接使用append方法将字典添加到列表中，如果需要更改字典中的数据，那么列表中的内容也会发生改变
                   #用.copy()就不会跟着改变
            name=json.dumps(goods) #将列表转字符串传给前端
            print(goods_list)
            print(name)
            return HttpResponse(name)
        elif action=='Save':
            back = 0
            add_goods=request.POST.get('name')
            models.Goods.objects.create(goodsname=add_goods)
            back = 1
            return HttpResponse(back)


def goodsCat(request):
    action=request.POST.get('action')
    if request.method=='GET':
        return render(request,'SystemSettings/goodsCat.html')
    else:
        goodsCat=[]
        if action == 'Load':
            goodsCat_list = models.GoodsCat.objects.all()
            value = {'value1': ''}  # 用字典和列表拼接很方便形成Json格式
            for row in goodsCat_list:
                value['value1'] = row.catname
                goodsCat.append(value.copy())  # 直接使用append方法将字典添加到列表中，如果需要更改字典中的数据，那么列表中的内容也会发生改变
                # 用.copy()就不会跟着改变
            name = json.dumps(goodsCat)  # 将列表转字符串传给前端
            return HttpResponse(name)
        elif action == 'Save':
            back = 0
            add_goodsCat = request.POST.get('name')
            back = 1
            models.GoodsCat.objects.create(catname=add_goodsCat)
            return HttpResponse(back)


def manufactor(request):
    action=request.POST.get('action')
    if request.method=='GET':
        column = get_4_column()
        return render(request, 'SystemSettings/manufactor.html', {'info_dict': column})
       # return render(request,'SystemSettings/manufactor.html')
    else:
        manufactor=[]
        if action == 'Load':
            Manufactor_list = models.Manufactor.objects.all()
            value = {'value1': '','value2':'','value3':'','value4':''}  # 用字典和列表拼接很方便形成Json格式
            for row in Manufactor_list:
                value['value1'] = row.name
                value['value2'] = row.manager
                value['value3'] = row.phone
                value['value4'] = row.address
                manufactor.append(value.copy())  # 直接使用append方法将字典添加到列表中，如果需要更改字典中的数据，那么列表中的内容也会发生改变
                # 用.copy()就不会跟着改变
            name = json.dumps(manufactor)  # 将列表转字符串传给前端
            return HttpResponse(name)
        elif action == 'Save':
            back = 0
            add_name = request.POST.get('name')
            add_manager=request.POST.get('manager')
            add_phone=request.POST.get('phone')
            add_address=request.POST.get('address')
            models.Manufactor.objects.create(name=add_name,phone=add_phone,manager=add_manager,address=add_address)
            back = 1
            return HttpResponse(back)
       # elif action == 'columns':
            pass

def supplier(request):
    action=request.POST.get('action')
    if request.method=='GET':
        return render(request,'SystemSettings/supplier.html')
    else:
        supplier=[]
        if action == 'LoadData':
            Supplier_list = models.Supplier.objects.all()
            value = {'value1': '','value2':'','value3':'','value4':''}  # 用字典和列表拼接很方便形成Json格式
            for row in Supplier_list:
                value['value1'] = row.name
                value['value2'] = row.managername
                value['value3'] = row.phone
                value['value4'] = row.address
                supplier.append(value.copy())  # 直接使用append方法将字典添加到列表中，如果需要更改字典中的数据，那么列表中的内容也会发生改变
                # 用.copy()就不会跟着改变
            name = json.dumps(supplier)  # 将列表转字符串传给前端
            return HttpResponse(name)
        elif action == 'Save':
            back = 0
            add_name = request.POST.get('name')
            add_manager=request.POST.get('manager')
            add_phone=request.POST.get('phone')
            add_address=request.POST.get('address')
            models.Supplier.objects.create(name=add_name,phone=add_phone,managername=add_manager,address=add_address)
            back = 1
            return HttpResponse(back)



#售卖页面  销售页面的处理函数
def Seller_Trans(request):
    cursor1 = connection.cursor();


    action = request.POST.get('action')
    if request.method == 'GET':
        return render(request, 'SystemSettings/Seller.html')
    else:
        seller = []
        if action == 'LoadData':
            #models.Seller.objects.all()
            Seller_list = models.Seller.objects.all()
            value = {'Sellername': '', 'Sellerphone': '', 'Sellerproperty': '', 'SellerOwner': '', 'SellerOwnerPhone': '', 'SellerOwnerLevel': '', 'SellerOwnerNo': '', 'SellerOwnerArea': ''}  # 用字典和列表拼接很方便形成Json格式
            for row in Seller_list:
                value['Sellername'] = row.Sellername
                value['Sellerphone'] = row.Sellerphone
                value['Sellerproperty'] = row.Sellerproperty
                value['SellerOwner'] = row.SellerOwner

                value['SellerOwnerPhone'] = row.SellerOwnerPhone
                value['SellerOwnerLevel'] = row.SellerOwnerLevel
                value['SellerOwnerNo'] = row.SellerOwnerNo
                value['SellerOwnerArea'] = row.SellerOwnerArea
                seller.append(value.copy())  # 直接使用append方法将字典添加到列表中，如果需要更改字典中的数据，那么列表中的内容也会发生改变
                # 用.copy()就不会跟着改变
            return HttpResponse(json.dumps(seller)) # 将列表转字符串传给前端
        elif action == 'Save':
            back = 0
            add_Sellername = request.POST.get('name')
            add_Sellerphone = '13098823498'
            add_Sellerproperty = request.POST.get('type')
            add_SellerOwner = request.POST.get('manager')

            add_SellerOwnerPhone = request.POST.get('phone')#request.POST.get('SellerOwnerPhone')
            add_SellerOwnerLevel = request.POST.get('floor')
            add_SellerOwnerNo = request.POST.get('number')
            add_SellerOwnerArea = request.POST.get('area')


            models.Seller.objects.create(Sellername=add_Sellername, Sellerphone=add_Sellerphone, Sellerproperty=add_Sellerproperty,
                                           SellerOwner=add_SellerOwner,SellerOwnerPhone=add_SellerOwnerPhone,
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
            return HttpResponse(json.dumps(value_list)) #这个地方暂时先不处理



#销售商的属性配置
def SellerProp_Trans(request):
    fun_call_db_proc()
    action = request.POST.get('action')
    if request.method == 'GET':
        return render(request, 'SystemSettings/SellerProperty.html')
    else:
        supplier = []
        if action == 'LoadData':
            #models.Seller.objects.all()
            Supplier_list =  models.SellerPorprety.objects.all()
            value = {'SellerpropertyType': '', 'ID': ''}  # 用字典和列表拼接很方便形成Json格式
            for row in Supplier_list:
                value['SellerpropertyType'] = row.SellerpropertyType
                value['ID'] = row.id

                supplier.append(value.copy())  # 直接使用append方法将字典添加到列表中，如果需要更改字典中的数据，那么列表中的内容也会发生改变
                # 用.copy()就不会跟着改变
            name = json.dumps(supplier)  # 将列表转字符串传给前端
            return HttpResponse(name)
        elif action == 'Save':
            add_Propretyname = request.POST.get('Proprety')
            models.SellerPorprety.objects.create(SellerpropertyType=add_Propretyname)

            return HttpResponse(1)
        elif action == 'LoadSellerCat':
            return HttpResponse(1) #这个地方暂时先不处理




'''
wangyu test

def fun_call_db_proc(request):
    models.Models
    django.db
    cursor1 = dbTrans.cursor()
    cursor1.execute("select * from Goods_Table")
    cursor.fetchall()
#    cursor1.execture()

'''