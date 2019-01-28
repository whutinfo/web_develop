""""已用类做了这几个函数  begin"""
'''
json_frame_construct：针对页面的get命令进行处理   拼接前端表格的column数据
参数column_name:字段名  column_cnt：列的数量   column_width：列的宽度  column_align：对齐格式
除 column_cnt 是int，其它都是列表格式  列表的长度 与 数量匹配
返回值：将送进来的字段名与相应的列的各种参数拼接成前端需要的json形式返回
'''
def json_frame_construct(column_name,column_cnt,column_width,column_align):
	column = []
	for i in range(column_cnt):
		value = 'value'+str(i)
		width = str(column_width[i]) + '%'
		json_frame={'field': value, 'title': column_name[i], 'width':width, 'align': column_align[i]}
		column.append(json_frame.copy())
	return column
	# [
    #     {'field': 'value1', 'title': '生产厂商名称', 'width': '18%', 'align': 'center'},
    #     {'field': 'value2', 'title': '负责人姓名', 'width': '10%', 'align': 'center'},
    #     {'field': 'value3', 'title': '负责人手机号', 'width': "12%", 'align': 'center'},
    #     {'field': 'value4', 'title': '联系地址', 'width': "20%", 'align': 'center'}]

    #construct json

'''
拼接 get命令下，针对列表模式下的页面结构 
databasename:数据库名  tablename：表名  columnname：字段名 columncnt：字段个数  columnwidth：宽度 columnalign：对齐格式
'''
def fun_Get_Cmd_Trans(databasename,tablename,columnname,columncnt,columnwidth,columnalign):
    l_column_name = []
    for i in range(columncnt):
        comment = fun_call_db_proc(databasename,tablename,columnname[i])  #获得表的该字段的注释 即为前端表格的中文列名  返回元组如：(ID,)
        l_column_name.append(comment[0])
    column=json_frame_construct(l_column_name,columncnt,columnwidth,columnalign) #将所有列的参数送进去拼接成json

    return column


'''
wangyu test
http://blog.sina.com.cn/s/blog_70dc706b0100oavh.html  这个是针对存储过程的调用方法
获得表的该字段的注释  返回元组如：(ID,)
'''
def fun_call_db_proc(database_str,table_str,column_str):
	from django.db import connection, transaction
	data2 = ''
	data2 = 'SELECT column_comment FROM INFORMATION_SCHEMA.Columns WHERE table_schema = "'  + database_str + '" AND table_name= "' + \
			 table_str + '" AND  column_name= "' + column_str + '"'
	cursor1 = connection.cursor()
	cursor1.execute(data2)
	data_str = cursor1.fetchone()
	return data_str

""""已用类做了这几个函数  end"""


class base_html_construct_trans(object):

	database_name = 'aliyun'
	def __init__(self, *var):
		self.param = var

	def encode(self):
		self.version = self.param[0]
		# self.table_name = ''
		# self.column_list = ''
		# self.width_list = ''
		# self.align_list = ''
		if self.version == 1:  # 针对第一种格式
			self.table_name = self.param[1]  # 要获取注释信息的表名  数据库中真实表名
			self.column_list = self.param[2]  # 要获取注释的字段名  数据库中真实字段名
			self.width_list = self.param[3]  # 列的宽度 元组
			self.align_list = self.param[4]  # 列的对齐格式  元组
		elif self.version == 2:  # 针对第二种数据格式
			self.table_name = self.param[1]  # 要获取注释信息的表名  数据库中真实表名
			self.column_list = self.param[2]  # 要获取注释的字段名  数据库中真实字段名
			self.width_list = self.param[3]  # 列的宽度 元组
			self.align_list = self.param[4]  # 列的对齐格式  元组

		self.fielddic = {}

	def fun_call_db_proc(self, database_str, table_str, column_str):
		from django.db import connection
		data2 = ''
		data2 = 'SELECT column_comment FROM INFORMATION_SCHEMA.Columns WHERE table_schema = "' + database_str + '" AND table_name= "' + \
		        table_str + '" AND  column_name= "' + column_str + '"'
		cursor1 = connection.cursor()
		cursor1.execute(data2)
		data_str = cursor1.fetchone()
		return data_str

	'''
	json_frame_construct：针对页面的get命令进行处理   拼接前端表格的column数据
	参数column_name:字段名  column_cnt：列的数量   column_width：列的宽度  column_align：对齐格式
	除 column_cnt 是int，其它都是列表格式  列表的长度 与 数量匹配
	返回值：将送进来的字段名与相应的列的各种参数拼接成前端需要的json形式返回
	'''
	def json_frame_construct(self,column_name,column_cnt,column_width,column_align ):
		column = []
		for i in range(column_cnt):
			value = 'value' + str(i)
			width = str(column_width[i]) + '%'
			json_frame = {'field': value, 'title': column_name[i], 'width':width, 'align': column_align[i]}
			column.append(json_frame.copy())
		return column

	# [
	#     {'field': 'value1', 'title': '生产厂商名称', 'width': '18%', 'align': 'center'},
	#     {'field': 'value2', 'title': '负责人姓名', 'width': '10%', 'align': 'center'},
	#     {'field': 'value3', 'title': '负责人手机号', 'width': "12%", 'align': 'center'},
	#     {'field': 'value4', 'title': '联系地址', 'width': "20%", 'align': 'center'}]

	# construct json

	'''
	拼接 get命令下，针对列表模式下的页面结构 
	databasename:数据库名  tablename：表名  columnname：字段名 columncnt：字段个数  columnwidth：宽度 columnalign：对齐格式
	'''

	def fun_Get_Cmd_Trans(self, columncnt):
		l_column_name = []
		for i in range(columncnt):
			comment = self.fun_call_db_proc(self.database_name, self.table_name,self.column_list[i])  # 获得表的该字段的注释 即为前端表格的中文列名  返回元组如：(ID,)
			l_column_name.append(comment[0])
		self.fielddic = self.json_frame_construct(l_column_name, columncnt, self.width_list, self.align_list)  # 将所有列的参数送进去拼接成json

		return self.fielddic


'''    
    cursor1.execute("select * from Goods_Table")
    data = cursor1.fetchone()
    for data1 in data:
        print(data1)
'''
#    cursor1.execture()

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


#已经不用的函数

'''
base_fun_get_demo : 实现对某个表中的特定字段，将其注释内容返回  即中文列名
形参：Model_Object  是特定表的字段  如： Model_Object= models.GoodsCat
返回值：字段名和字段的注释内容，返回类型为字典
该函数也不用了
'''
def base_fun_get_demo(Model_Object):  # Model_Object= models.GoodsCat
    fielddic = {}
    table_name = Model_Object._meta.db_table  #获取该Model对象的表名
    for field in Model_Object._meta.fields:
        var = field.get_attname_column()#获取当前列的列名  ( model field ，db_column)形式 (models中写定的列名，实际数据库中的列名)
        field_name = var[0]
        db_column = var[1]
        comment = fun_call_db_proc('aliyun', table_name, db_column)  #<class 'tuple'>: ('索引号',)
        fielddic[field_name] = comment[0]
    return fielddic


'''
 针对页面的get命令进行处理 获取前cnt列列名  包括id  但是前端页面不会显示id 处理信息用
 cnt:列的数量
 var：()元组格式 以 列的宽度，对齐格式 的顺序传进来
 '''
'''
该函数不用了  替换成fun_Get_Cmd_Trans
def get_cnt_column(cnt,*var):
    j_str = []  #最终返回的column列的所有参数，json格式
    width_list = var[0] #列的宽度 元组
    align_list = var[1] #列的对齐格式  元组
    model_name = var[2] #要获取注释信息的model对象
    var = base_fun_get_demo(model_name)   #获取该表中所有的列名及其对应的注释，注释即为最后要展示的列名
    #{'id': '索引号', 'name': '生产厂商名称', 'manager': '负责人名称', 'phone': '负责人联系电话', 'address': '生产厂商地址'}
    i = 0
    for key,value in var.items():
        if i != cnt:
            # 构建列的HTML命令
            # comment + head_pre ......
            j_str = json_frame_construct(j_str, key, value, width_list[i], align_list[i])
            # 每一次往j_str添加一列json数据
        i += 1

    return j_str
'''

#已经不用的函数