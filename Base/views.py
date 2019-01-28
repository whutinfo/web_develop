from django.shortcuts import render
from django.shortcuts import HttpResponse
from Models import models
from Base.com_func import *
import json


'''
公共函数在Base下的com_func中，不要动！只需在自己的views下 from Base.com_func import * 导入即可

单页的页面函数在Base下的views中，复制到自己写的app下的views中做相应的更改
保存需要读取前端Save传值写的那些参数  具体看前端save函数  有注释

单页的页面html 在 Base/templates/Base/sample_single.html  全部替换到自己的页面中
'''


'''页面函数'''
def Base(request):
	action = request.POST.get('action')

	'''sys code define variable begin  '''
	column = ''
	'''sys code define variable begin  '''

	if request.method == 'GET':
		'''user code define variable begin  '''

		databasename = 'aliyun'
		tablename = 'Manufactor_Table'  # 在数据库找到想要获取字段的表，应为数据库中真实表名，即Models中的db_table
		''' id(数据库中自增长的那个字段，同样应为真实字段名)一定要有！！并放在第一个，不是用来显示，用来处理信息  其余顺序根据前端想要的摆放顺序来'''
		columnname = ['id', 'name','managerName','phone','address']  # 在数据库找到想要获取的字段，应为数据库中真实的字段名,即Models中的db_column，如有的话
		columncnt = 5  # 需要获取的列的数量 包括id
		columnwidth = [0, 18,10,12,20]  # 列的宽度 个数与cnt匹配
		columnalign = ['center'] * columncnt  # 对齐格式 个数与cnt匹配   可以不用改！！

		'''user code define variable  end  '''

		'''sys code begin  '''
		column = fun_Get_Cmd_Trans(databasename, tablename, columnname, columncnt, columnwidth, columnalign)
		'''sys code end'''

		'''usr code begin  '''
		return render(request, 'Base/sample_single.html', {'info_dict': column})
		'''usr code end '''

	else:
		'''user code define variable begin  '''
		model_name = models.Manufactor  # 想要展示的表的Model对象
		'''user code define variable end  '''

		'''usr code begin  '''

		if action == 'LoadData':
			querys = model_name.objects.all()  # 获取需要的字段名的数据
			value_dict = {'value0':'','value1': '', 'value2': '','value3':'','value4':''}   #有几个需要的列就有多少value 包括Id
			value_list = []
			for row in querys:
				value_dict['value0'] = row.id  # 一定要获取id 并放进第一个value0
				value_dict['value1'] = row.name  # 根据前端想要的摆放顺序来
				value_dict['value2'] = row.manager  #负责人姓名
				value_dict['value3'] = row.phone    #负责人联系电话
				value_dict['value4'] = row.address  #生产厂商地址
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
