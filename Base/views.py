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
