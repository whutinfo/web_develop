from django.shortcuts import render
from django.shortcuts import HttpResponse
from Models import models
import json

# Create your views here.
def customermanager(request):
    action=request.POST.get('action')
    if request.method=='GET':
        return render(request, 'customermanager/customermanager.html')
    else:
        customermanager=[]
        if action == 'LoadData':
            customermanager_list = models.Customermanager.objects.all()
            value = {'value1': '','value2':'','value3':'','value4':'','value5':'','value6':'','value7':'','value8':''}  # 用字典和列表拼接很方便形成Json格式
            for row in customermanager_list:
                value['value1'] = row.name
                value['value2'] = row.birthday
                value['value3'] = row.sex
                value['value4'] = row.phone
                value['value5'] = row.carid
                value['value6'] = row.point
                value['value7'] = row.create_time
                value['value8'] = row.update_time
                customermanager.append(value.copy())  # 直接使用append方法将字典添加到列表中，如果需要更改字典中的数据，那么列表中的内容也会发生改变
                # 用.copy()就不会跟着改变

            return HttpResponse(json.dumps(customermanager)) # 将列表转字符串传给前端
        elif action == 'Save':
            add_name = request.POST.get('name')
            add_birthday=request.POST.get('birthday')
            add_sex=request.POST.get('sex')
            add_phone=request.POST.get('phone')
            add_carid = request.POST.get('carid')
            add_point = request.POST.get('point')
            add_create_time = request.POST.get('create_time')
            add_update_time = request.POST.get('update_time')
            models.Customermanager.objects.create(name=add_name,birthday=add_birthday,sex=add_sex,phone=add_phone,carid=add_carid,point=add_point,create_time=add_create_time,update_time=add_update_time,)

            return HttpResponse(1)
