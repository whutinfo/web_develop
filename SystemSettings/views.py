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
            add_goods=request.POST.get('name')
            models.Goods.objects.create(goodsname=add_goods)
            return HttpResponse(1)


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
            add_goodsCat = request.POST.get('name')
            models.GoodsCat.objects.create(catname=add_goodsCat)
            return HttpResponse(1)


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
            add_name = request.POST.get('name')
            add_manager=request.POST.get('manager')
            add_phone=request.POST.get('phone')
            add_address=request.POST.get('address')
            models.Manufactor.objects.create(name=add_name,phone=add_phone,manager=add_manager,address=add_address)

            return HttpResponse(1)
        return HttpResponse()


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
            add_name = request.POST.get('name')
            add_manager=request.POST.get('manager')
            add_phone=request.POST.get('phone')
            add_address=request.POST.get('address')
            models.Supplier.objects.create(name=add_name,phone=add_phone,managername=add_manager,address=add_address)

            return HttpResponse(1)
        return HttpResponse()



