from django.shortcuts import render
from django.http import HttpResponse


def mainIndex(request):# request  接收的请求
    # return HttpResponse('hello world')  #返回字符串
    return render(request, 'MainIndex/main.html')##用render，从第二个参数中找
