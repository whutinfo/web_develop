from django.shortcuts import render
from django.http import HttpResponse
from Models import models
import json

def index(request):
    if request.method == 'GET':
        return render(request, 'video/demo.html')
    else:
        action = request.POST.get('action')
        if action == 'LoadData':
            value_dict = {'value1': '', 'value2': '', 'value3': '', 'value4': '', 'value5': '', 'value6': '',
                          'value7': '', }
            value_list = []
            videos = models.Video.objects.all()
            for v in videos:
                value_dict['value1'] = v.id
                value_dict['value2'] = v.ip
                value_dict['value3'] = v.port
                value_dict['value4'] = v.name
                value_dict['value5'] = v.pwd
                value_dict['value6'] = v.rtsp_port
                value_dict['value7'] = v.stream_type
                value_list.append(value_dict.copy())
            return HttpResponse(json.dumps(value_list))
