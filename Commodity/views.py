from django.shortcuts import render
from django.shortcuts import HttpResponse
from Models import models
import json

# Create your views here.
def stockIn(request):
	if request.method == 'GET':
		return render(request,'Commodity/stockIn.html')
	else:
		action = request.POST.get('action')
		pass

def stockOut(request):
	if request.method == 'GET':
		return render(request,'Commodity/stockOut.html')
	else:
		action = request.POST.get('action')
		pass

def Load_Commodity(request):
	if request.method == 'GET':
		return render(request,'Commodity/commodity.html')
	else:
		action = request.POST.get('action')
		pass