from django.shortcuts import render
from django.shortcuts import HttpResponse
import json


def Base(request):
	action = request.POST.get('action')
	if action == 'columns':
		value_list = [{'field': 'CK', 'title': '', 'checkbox': 'true', 'width': "5%"},
	                {'field': 'value1', 'title': '生产厂商名称', 'width': '18%', 'align': 'center'},
	                {'field': 'value2', 'title': '负责人姓名', 'width': '10%', 'align': 'center'},
	                {'field': 'value3', 'title': '负责人手机号', 'width': "12%", 'align': 'center'},
	                {'field': 'value4', 'title': '联系地址', 'width': "20%", 'align': 'center'}]
		return HttpResponse(json.dumps(value_list))


'''
json_frame_construct：拼接前端表格的column数据   为了width 和align是可变的 改成每次拼接一列json返回
参数var  如： ('id', '索引号', 18, 'center') 元组参数  field名称，实际展示的名称，该列宽度，对齐格式
返回值：更新送进来的第一个参数[]，将{}字典添加 拼接成Json 
'''
def json_frame_construct(*var):#<class 'tuple'>: ('id', '索引号', 18, 'center')
    column = var[0]
    value = var[1]
    title = var[2]
    width = str(var[3])+'%'
    align = 'center'
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
形参：Model_Object  是特定表的字段  如： Model_Object= models.GoodsCat
返回值：字段名和字段的注释内容，返回类型为字典
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
wangyu test
http://blog.sina.com.cn/s/blog_70dc706b0100oavh.html  这个是针对存储过程的调用方法
获得表的注释字段
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