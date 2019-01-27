from django.shortcuts import render
from django.shortcuts import HttpResponse

from Models import models
import json
from Base.views import *


def goods(request):
    action = request.POST.get('action')
    if request.method == 'GET':
        """  可以改参数的地方  """
        cnt = 2  #需要获取的列的数量  包括id 按顺序获取
        width_list = [0,15]   #列的宽度  个数与cnt匹配  顺序对应数据库中列的顺序  id不展示，但会获取，赋0
        align_list = ['center']*cnt  #对齐格式 个数与cnt匹配   顺序对应数据库中列的顺序  id不展示，但会获取
        model_name = models.Goods   #想要展示的表的Model对象
        """  可以改参数的地方  """

        column = get_cnt_column(cnt,width_list,align_list,model_name)
        return render(request, 'SystemSettings/goods.html', {'info_dict': column})

    else:
        """  可以改参数的地方  """
        model_name = models.Goods  # 想要展示的表的Model对象
        """  可以改参数的地方  """

        if action=='LoadData':
            goods_list=model_name.objects.all()
            value = base_fun_get_demo(model_name)  # 获取该表中所有的列名及其对应的注释，即对应前端的{ field : name }
            index = tuple(value) #转元组
            '''
			加载显示数据时返回的字典的Key要跟前端的field匹配，故通过base_fun_get_demo返回字典，并将其对应的value改成想要的数据
			用字典和列表拼接很方便形成Json格式
			value={'id': '索引号', 'name': '生产厂商名称', 'manager': '负责人名称', 'phone': '负责人联系电话', 'address': '生产厂商地址'}
		   '''
            value_list = []
            for row in goods_list:
                value[index[0]] = row.id
                value[index[1]]=row.goodsname  # [{},{},{}]
                value_list.append(value.copy())  #直接使用append方法将字典添加到列表中，如果需要更改字典中的数据，那么列表中的内容也会发生改变
                   #用.copy()就不会跟着改变

            return HttpResponse(json.dumps(value_list))#将列表拼字典仿Json格式转字符串传给前端
        elif action=='Save':
            back = 0
            add_goods=request.POST.get('name')
            models.Goods.objects.create(goodsname=add_goods)
            back = 1
            return HttpResponse(back)


def goodsCat(request):
    action=request.POST.get('action')
    if request.method=='GET':
        """  可以改参数的地方  """
        cnt = 2  # 需要获取的列的数量  包括id 按顺序获取
        width_list = [0, 15]  # 列的宽度  个数与cnt匹配  顺序对应数据库中列的顺序  id不展示，但会获取，赋0
        align_list = ['center'] * cnt  # 对齐格式 个数与cnt匹配   顺序对应数据库中列的顺序  id不展示，但会获取
        model_name = models.GoodsCat  # 想要展示的表的Model对象
        """  可以改参数的地方  """

        column = get_cnt_column(cnt, width_list, align_list, model_name)
        return render(request, 'SystemSettings/goodsCat.html', {'info_dict': column})
    else:
        """  可以改参数的地方  """
        model_name = models.GoodsCat  # 想要展示的表的Model对象
        """  可以改参数的地方  """

        if action == 'LoadData':
            goodsCat_list = model_name.objects.all()
            value = base_fun_get_demo(model_name)  # 获取该表中所有的列名及其对应的注释，即对应前端的{ field : name }
            index = tuple(value)
            '''
			加载显示数据时返回的字典的Key要跟前端的field匹配，故通过base_fun_get_demo返回字典，并将其对应的value改成想要的数据
			用字典和列表拼接很方便形成Json格式
			value={'id': '索引号', 'name': '生产厂商名称', 'manager': '负责人名称', 'phone': '负责人联系电话', 'address': '生产厂商地址'}
		   '''
            value_list = []
            for row in goodsCat_list:
                value[index[0]] = row.id
                value[index[1]] = row.catname
                value_list.append(value.copy())  # 直接使用append方法将字典添加到列表中，如果需要更改字典中的数据，那么列表中的内容也会发生改变
                # 用.copy()就不会跟着改变
            return HttpResponse(json.dumps( value_list))  # 将列表转字符串传给前端
        elif action == 'Save':
            back = 0
            add_goodsCat = request.POST.get('name')
            back = 1
            models.GoodsCat.objects.create(catname=add_goodsCat)
            return HttpResponse(back)


def manufactor(request):
    action=request.POST.get('action')
    if request.method=='GET':
        """  可以改参数的地方  """
        cnt = 5  #需要获取的列的数量  包括id 按顺序获取
        width_list = [0,18, 10, 15, 20]   #列的宽度  个数与cnt匹配  顺序对应数据库中列的顺序  id不展示，但会获取，赋0
        align_list = ['center']*cnt  #对齐格式 个数与cnt匹配   顺序对应数据库中列的顺序  id不展示，但会获取
        model_name = models.Manufactor   #想要展示的表的Model对象
        """  可以改参数的地方  """

        column = get_cnt_column(cnt,width_list,align_list,model_name)
        return render(request, 'SystemSettings/manufactor.html', {'info_dict': column})
    else:
        """  可以改参数的地方  """
        model_name = models.Manufactor  # 想要展示的表的Model对象
        """  可以改参数的地方  """
        if action == 'LoadData':
            Manufactor_list = model_name.objects.all()
            value = base_fun_get_demo(model_name)#获取该表中所有的列名及其对应的注释，即对应前端的{ field : name }
            index = tuple(value)
            value_list = []
            '''
            加载显示数据时返回的字典的Key要跟前端的field匹配，故通过base_fun_get_demo返回字典，并将其对应的value改成想要的数据
            用字典和列表拼接很方便形成Json格式
            value={'id': '索引号', 'name': '生产厂商名称', 'manager': '负责人名称', 'phone': '负责人联系电话', 'address': '生产厂商地址'}
           '''
            for row in Manufactor_list:
                value[index[0]] = row.id
                value[index[1]] = row.name
                value[index[2]] = row.manager
                value[index[3]] = row.phone
                value[index[4]] = row.address
                value_list.append(value.copy())  # 直接使用append方法将字典添加到列表中，如果需要更改字典中的数据，那么列表中的内容也会发生改变
                # 用.copy()就不会跟着改变
            return HttpResponse(json.dumps(value_list))  # 将列表转字符串传给前端
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
        """  可以改参数的地方  """
        cnt = 5  # 需要获取的列的数量  包括id 按顺序获取
        width_list = [0, 18, 10, 12, 20]  # 列的宽度  个数与cnt匹配  顺序对应数据库中列的顺序  id不展示，但会获取，赋0
        align_list = ['center'] * cnt  # 对齐格式 个数与cnt匹配   顺序对应数据库中列的顺序  id不展示，但会获取
        model_name = models.Supplier  # 想要展示的表的Model对象
        """  可以改参数的地方  """

        column = get_cnt_column(cnt, width_list, align_list, model_name)
        return render(request, 'SystemSettings/supplier.html', {'info_dict': column})

    else:
        """  可以改参数的地方  """
        model_name = models.Supplier  # 想要展示的表的Model对象
        """  可以改参数的地方  """
        if action == 'LoadData':
            Supplier_list = model_name.objects.all()
            value = base_fun_get_demo(model_name)  # 获取该表中所有的列名及其对应的注释，即对应前端的{ field : name }
            index = tuple(value)
            value_list = []
            '''
			加载显示数据时返回的字典的Key要跟前端的field匹配，故通过base_fun_get_demo返回字典，并将其对应的value改成想要的数据
			用字典和列表拼接很方便形成Json格式
			value={'id': '索引号', 'name': '生产厂商名称', 'manager': '负责人名称', 'phone': '负责人联系电话', 'address': '生产厂商地址'}
		   '''
            for row in Supplier_list:
                value[index[0]] = row.id
                value[index[1]] = row.name
                value[index[2]] = row.managername
                value[index[3]] = row.phone
                value[index[4]] = row.address
                value_list.append(value.copy())  # 直接使用append方法将字典添加到列表中，如果需要更改字典中的数据，那么列表中的内容也会发生改变
                # 用.copy()就不会跟着改变

            return HttpResponse(json.dumps(value_list)) # 将列表转字符串传给前端
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
        """  可以改参数的地方  """
        cnt = 8  # 需要获取的列的数量  包括id 按顺序获取
        width_list = [0, 18, 15, 12, 12, 12, 12, 12]  # 列的宽度  个数与cnt匹配  顺序对应数据库中列的顺序  id不展示，但会获取，赋0
        align_list = ['center'] * cnt  # 对齐格式 个数与cnt匹配   顺序对应数据库中列的顺序  id不展示，但会获取
        model_name = models.Seller  # 想要展示的表的Model对象
        """  可以改参数的地方  """

        column = get_cnt_column(cnt, width_list, align_list, model_name)
        return render(request, 'SystemSettings/Seller.html', {'info_dict': column})
    else:
        """  可以改参数的地方  """
        model_name = models.Seller  # 想要展示的表的Model对象
        """  可以改参数的地方  """
        if action == 'LoadData':
            Seller_list = model_name.objects.all()
            value = base_fun_get_demo(model_name)  # 获取该表中所有的列名及其对应的注释，即对应前端的{ field : name }
            index = tuple(value)
            value_list = []
            '''
			加载显示数据时返回的字典的Key要跟前端的field匹配，故通过base_fun_get_demo返回字典，并将其对应的value改成想要的数据
			用字典和列表拼接很方便形成Json格式
			value={'id': '索引号', 'name': '生产厂商名称', 'manager': '负责人名称', 'phone': '负责人联系电话', 'address': '生产厂商地址'}
		   '''
           # value = {'Sellername': '', 'Sellerphone': '', 'Sellerproperty': '', 'SellerOwner': '', 'SellerOwnerPhone': '', 'SellerOwnerLevel': '', 'SellerOwnerNo': '', 'SellerOwnerArea': ''}  # 用字典和列表拼接很方便形成Json格式
            for row in Seller_list:
                value[index[1]] = row.Sellername
                value[index[2]] = row.Sellerproperty
                value[index[3]] = row.SellerOwner
                value[index[4]] = row.SellerOwnerPhone
                value[index[5]] = row.SellerOwnerLevel
                value[index[6]] = row.SellerOwnerNo
                value[index[7]] = row.SellerOwnerArea
                value_list.append(value.copy())  # 直接使用append方法将字典添加到列表中，如果需要更改字典中的数据，那么列表中的内容也会发生改变
                # 用.copy()就不会跟着改变
            return HttpResponse(json.dumps(value_list)) # 将列表转字符串传给前端
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
            return HttpResponse(json.dumps(value_list)) #这个地方暂时先不处理



#销售商的属性配置
def SellerProp_Trans(request):
    fun_call_db_proc()
    action = request.POST.get('action')
    if request.method == 'GET':
        """  可以改参数的地方  """
        cnt = 2  # 需要获取的列的数量  包括id 按顺序获取
        width_list = [0, 18]  # 列的宽度  个数与cnt匹配  顺序对应数据库中列的顺序  id不展示，但会获取，赋0
        align_list = ['center'] * cnt  # 对齐格式 个数与cnt匹配   顺序对应数据库中列的顺序  id不展示，但会获取
        model_name = models.SellerPorprety # 想要展示的表的Model对象
        """  可以改参数的地方  """

        column = get_cnt_column(cnt, width_list, align_list, model_name)
        return render(request, 'SystemSettings/SellerProperty.html', {'info_dict': column})
    else:
        """  可以改参数的地方  """
        model_name = models.SellerPorprety  # 想要展示的表的Model对象
        """  可以改参数的地方  """
        if action == 'LoadData':
            SellerProp_list = model_name.objects.all()
            value = base_fun_get_demo(model_name)  # 获取该表中所有的列名及其对应的注释，即对应前端的{ field : name }
            index = tuple(value)
            value_list = []
            '''
			加载显示数据时返回的字典的Key要跟前端的field匹配，故通过base_fun_get_demo返回字典，并将其对应的value改成想要的数据
			用字典和列表拼接很方便形成Json格式
			value={'id': '索引号', 'name': '生产厂商名称', 'manager': '负责人名称', 'phone': '负责人联系电话', 'address': '生产厂商地址'}
		   '''
          #  value = {'SellerpropertyType': '', 'ID': ''}  # 用字典和列表拼接很方便形成Json格式
            for row in SellerProp_list:
                value[index[0]] = row.id
                value[index[1]] = row.SellerpropertyType
                value_list.append(value.copy())  # 直接使用append方法将字典添加到列表中，如果需要更改字典中的数据，那么列表中的内容也会发生改变
                # 用.copy()就不会跟着改变
            return HttpResponse(json.dumps(value_list)  ) # 将列表转字符串传给前端
        elif action == 'Save':
            add_Propretyname = request.POST.get('Proprety')
            models.SellerPorprety.objects.create(SellerpropertyType=add_Propretyname)
            return HttpResponse(1)



