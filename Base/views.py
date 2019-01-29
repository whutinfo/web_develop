from django.shortcuts import render
from django.shortcuts import HttpResponse
from Models import models
from Base.com_func import *
import json


'''
将想要在前端展示的相应字段的中文名写到数据库中对应的注释里
公共函数在Base下的com_func中，不要动！只需在自己的views下 from Base.com_func import * 导入即可

单页的页面函数在Base下的views中，复制到自己写的app下的views中做相应的更改
保存需要读取前端Save传值写的那些参数  具体看前端save函数  有注释

单页的页面html 在 Base/templates/Base/sample_single.html  全部替换到自己的页面中
'''


'''页面函数'''
def Sample_Singe(request):
	action = request.POST.get('action')

	'''sys code define variable begin  '''
	column = ''

	'''sys code define variable end  '''

	if request.method == 'GET':
		'''user code define variable begin  '''
		''' !!  都只改值，不动变量名    !!'''
		html_name = 'Base/sample_single.html' #配置html的所在地址
		head_title = '' #  网页的标题title

		'''!!    表格初始化    !! '''
		datagrid_version  = 1  #哪一代版本的 int
		datagrid_title = '生产厂商信息'  #表格的名称
		datagrid_tablename = 'Manufactor_Table'  # 在数据库找到想要获取字段的表，应为数据库中真实表名，即Models中的db_table
		''' id(数据库中自增长的那个字段，同样应为真实字段名)一定要有！！并放在第一个，不是用来显示，用来处理信息  其余顺序根据前端想要的摆放顺序来'''
		datagrid_columnname = ['id', 'name','managerName','phone','address']  # 在数据库找到想要获取的字段，应为数据库中真实的字段名,即Models中的db_column，如有的话
		datagrid_columncnt = 5  # 需要获取的列的数量 包括id
		datagrid_columnwidth = [0, 18, 10, 12, 20]  # 列的宽度 个数与cnt匹配
		datagrid_columnalign = ['center'] * datagrid_columncnt  # 对齐格式 个数与cnt匹配   可以不用改！！

		''' !!  新增数据时的弹框初始化    新增数据是不需要传id这个参数的  id是新增后生成的自增长字段      !! '''
		add_tab_version = 1
		add_tab_title = '新增生产厂商'
		add_tab_tablename = 'Manufactor_Table'  # 在数据库找到想要获取字段的表，应为数据库中真实表名，即Models中的db_table
		add_tab_columnname = ['name', 'managerName',
		                      'phone', 'address']  # 在数据库找到想要获取的字段，应为数据库中真实的字段名,即Models中的db_column，如有的话
		add_tab_columncnt = 4  # 需要获取的列的数量 不包括id！
		add_tab_boxtype = [1] * add_tab_columncnt
		'''user code define variable  end  '''

		'''sys code begin  '''

		'''        表格初始化      '''
		base_html_construct = base_html_construct_trans(datagrid_version , datagrid_tablename,datagrid_columnname,datagrid_columnwidth,datagrid_columnalign)
		base_html_construct.encode() #先将传送进来的参数进行解析
		column = base_html_construct.fun_Get_Cmd_Trans(datagrid_columncnt) #拼接cnt列Json
		'''  新增数据时的弹框初始化     '''
		add_tab_construct = add_tab_construct_trans(add_tab_version, add_tab_tablename, add_tab_columnname, add_tab_boxtype)
		add_tab_construct.encode()  # 先将传送进来的参数进行解析
		add_tab_dict = add_tab_construct.fun_Get_Cmd_Trans(add_tab_columncnt)  # 拼接cnt列Json

		return_dict = {'head_title':head_title,'info_dict': column,'datagrid_title':datagrid_title,'add_dict':add_tab_dict,'add_title':add_tab_title}

		return render(request, html_name,return_dict)#将初始化信息全部返回到前端
		'''sys code end'''

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




def Sample_Div(request):
	action = request.POST.get('action')

	'''sys code define variable begin  '''
	column = ''
	'''sys code define variable begin  '''

	if request.method == 'GET':
		'''user code define variable begin  '''
		html_name = 'Base/sample_div.html' #配置html的所在地址
		head_title = '' #  网页的标题title


		'''!!    上表格初始化    !! '''
		top_datagrid_version = 1  #哪一种初始化 int
		top_datagrid_title = '生产厂商信息'  #表格的名称
		top_datagrid_tablename = 'Manufactor_Table'  # 在数据库找到想要获取字段的表，应为数据库中真实表名，即Models中的db_table
		''' id(数据库中自增长的那个字段，同样应为真实字段名)一定要有！！并放在第一个，不是用来显示，用来处理信息  其余顺序根据前端想要的摆放顺序来'''
		top_datagrid_columnname = ['id', 'name','managerName','phone','address']  # 在数据库找到想要获取的字段，应为数据库中真实的字段名,即Models中的db_column，如有的话
		top_datagrid_columncnt = 5  # 需要获取的列的数量 包括id
		top_datagrid_columnwidth = [0, 18, 10, 12, 20]  # 列的宽度 个数与cnt匹配
		top_datagrid_columnalign = ['center'] * top_datagrid_columncnt  # 对齐格式 个数与cnt匹配   可以不用改！！

		'''!!    下表格初始化    !! '''
		below_datagrid_version  = 1  #哪一种初始化 int
		below_datagrid_title = '生产厂商详情'  # 表格的名称
		below_datagrid_tablename = 'Manufactor_Table'  # 在数据库找到想要获取字段的表，应为数据库中真实表名，即Models中的db_table
		''' id(数据库中自增长的那个字段，同样应为真实字段名)一定要有！！并放在第一个，不是用来显示，用来处理信息  其余顺序根据前端想要的摆放顺序来'''
		below_datagrid_columnname = ['id', 'name', 'managerName', 'phone',
		                           'address']  # 在数据库找到想要获取的字段，应为数据库中真实的字段名,即Models中的db_column，如有的话
		below_datagrid_columncnt = 5  # 需要获取的列的数量 包括id
		below_datagrid_columnwidth = [0, 18, 10, 12, 20]  # 列的宽度 个数与cnt匹配
		below_datagrid_columnalign = ['center'] * top_datagrid_columncnt  # 对齐格式 个数与cnt匹配   可以不用改！！


		''' !!  新增数据时的弹框初始化    新增数据是不需要传id这个参数的  id是新增后生成的自增长字段      !! '''
		add_tab_version = 1    #版本号
		add_tab_title = '新增生产厂商'
		add_tab_tablename = 'Manufactor_Table'  # 在数据库找到想要获取字段的表，应为数据库中真实表名，即Models中的db_table
		add_tab_columnname = ['name', 'managerName',
		                      'phone', 'address']  # 在数据库找到想要获取的字段，应为数据库中真实的字段名,即Models中的db_column，如有的话
		add_tab_columncnt = 4  # 需要获取的列的数量 不包括id！
		add_tab_boxtype = [1]*add_tab_columncnt  # 是 1:输入框textbox,还是 2:下拉框combobox,还是 3 :日历datebox
		'''user code define variable  end  '''

		'''sys code begin  '''

		'''        上表格初始化      '''
		top_datagrid_construct = base_html_construct_trans(top_datagrid_version ,top_datagrid_tablename,top_datagrid_columnname,
		                                                   top_datagrid_columnwidth,top_datagrid_columnalign)
		top_datagrid_construct.encode() #先将传送进来的参数进行解析
		column = top_datagrid_construct.fun_Get_Cmd_Trans(top_datagrid_columncnt) #拼接cnt列Json

		'''        下表格初始化      '''
		below_datagrid_construct = base_html_construct_trans(below_datagrid_version , below_datagrid_tablename, below_datagrid_columnname,
		                                                     below_datagrid_columnwidth, below_datagrid_columnalign)
		below_datagrid_construct.encode()  # 先将传送进来的参数进行解析
		detail_dict = below_datagrid_construct.fun_Get_Cmd_Trans(below_datagrid_columncnt)  # 拼接cnt列Json

		'''  新增数据时的弹框初始化     '''
		add_tab_construct = add_tab_construct_trans(add_tab_version, add_tab_tablename, add_tab_columnname, add_tab_boxtype)
		add_tab_construct.encode()  # 先将传送进来的参数进行解析
		add_tab_dict = add_tab_construct.fun_Get_Cmd_Trans(add_tab_columncnt)  # 拼接cnt列Json

		return_dict = {'head_title':head_title, 'info_dict': column, 'datagrid_title':top_datagrid_title,
		               'detail_dict':detail_dict, 'detail_name':below_datagrid_title, 'add_dict':add_tab_dict, 'add_title':add_tab_title}

		return render(request, html_name,return_dict)#将初始化信息全部返回到前端

		'''sys code end  '''

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
			''' user code begin '''
			add_goods = request.POST.get('name')
			models.Goods.objects.create(goodsname=add_goods)
			''' user code end '''
			back = 1
			return HttpResponse(back)

		elif action == 'LoadDetail':
			value_id =  request.POST.get('value_id')
			querys = model_name.objects.filter(pk = value_id)  # 获取需要的字段名的数据
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

		'''usr code end '''
