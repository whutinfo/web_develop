from django.shortcuts import render
from django.shortcuts import HttpResponse
from Models import models
import json


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
        return render(request,'SystemSettings/manufactor.html')
    else:
        manufactor=[]
        if action == 'Load':
            Manufactor_list = models.Manufactor.objects.all()
            value = {'value1': '','value2':'','value3':'','value4':''}  # 用字典和列表拼接很方便形成Json格式
            for row in Manufactor_list:
                print(row.name,row.address,row.manager,row.phone)
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



