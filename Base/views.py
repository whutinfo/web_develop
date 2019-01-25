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

def get_checkbox(type):
	value_dict = {}
	value_list = []
	if type == 'datagrid':  # 表格形式 统一加载checkbox 固定宽度5%
		value_dict['field'] = 'CK'
		value_dict['checkbox'] = 'true'
		value_dict['width'] = '5%'
		value_list.append(value_dict.copy())
		value_dict.clear()
		return value_list

def get_columns(list,**var):#字典形式传参
	#  {'field': 'CK', 'title': '', 'checkbox': 'true', 'width': '5%'}
	value_dict = {}
	value_list = list

	value_dict['field'] = var['field']
	value_dict['title'] = var['title']
	value_dict['width'] = var['width']
	value_dict['align'] = var['align']
	value_list.append(value_dict.copy())
	value_dict.clear()
	return value_list
	# value_list = [{'field': 'CK', 'title': '', 'checkbox': 'true', 'width': "5%"},
    #               {'field': 'value1', 'title': '生产厂商名称', 'width': '18%', 'align': 'center'},
    #               {'field': 'value2', 'title': '负责人姓名', 'width': '10%', 'align': 'center'},
    #               {'field': 'value3', 'title': '负责人手机号', 'width': "12%", 'align': 'center'},
    #               {'field': 'value4', 'title': '联系地址', 'width': "20%", 'align': 'center'}]
