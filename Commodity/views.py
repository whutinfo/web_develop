from django.shortcuts import render
from django.shortcuts import HttpResponse
from Models import models
import json
import datetime
import time
# Create your views here.
def stockIn(request):
	user_id = request.session.get("Login_UserId")
	if request.method == 'GET':
		return render(request,'Commodity/stockIn.html')
	else:
		action = request.POST.get('action')
		if action == 'LoadData':
			value_dict = {'value1':'','value2':'','value3':'','value4':'','value5':'','value6':'',
			              'value7': '','value8':'','value9':'','value10':'','value11':'','value12':'',}
			# 入库单编号 商品名称 商品类型 条形码 入库数量 进货总价 保质期限 进库商户 操作人 入库时间 生产厂家 供货商
			value_list = []
			stock_Ins = models.StockIn.objects.all()
			for stock_in in stock_Ins:
				value_dict['value1'] = str(stock_in.stockin_id).zfill(9) # 入库单编号
				if stock_in.goods != None:
					value_dict['value2'] = stock_in.goods.goodsname    # 商品名称
				else:
					value_dict['value2'] = ''
				if stock_in.cat != None:
					value_dict['value3'] = stock_in.cat.catname      #商品类型
				else:
					value_dict['value3'] = ''
				value_dict['value4'] = stock_in.goods_sn        #条形码
				value_dict['value5'] = stock_in.in_amount     #入库数量
				value_dict['value6'] = stock_in.cost         # 进货总价
				goodsInfo = stock_in.goodsinfo_set.filter(stockin_id=stock_in.id)   # 保质期限
				if goodsInfo.count() != 0:
					value_dict['value7'] = goodsInfo.first().exp_date
				else:
					value_dict['value7'] = ''
				if stock_in.seller != None:
					value_dict['value8'] = stock_in.seller.Sellername  # 进库商户
				else:
					value_dict['value8'] = ''
				if stock_in.performer != None:
					value_dict['value9'] = stock_in.performer.name  # 操作人
				else:
					value_dict['value9'] = ''
				print(stock_in.in_time)
				value_dict['value10'] = stock_in.in_time.strftime("%Y-%m-%d %H:%M:%S")   # 入库时间
				if stock_in.manufactor != None:
					value_dict['value11'] = stock_in.manufactor.name  # 生产厂家
				else:
					value_dict['value11'] = ''
				if stock_in.supplier != None:
					value_dict['value12'] = stock_in.supplier.name  # 供货商
				else:
					value_dict['value12'] = ''
				value_list.append(value_dict.copy())
			return HttpResponse(json.dumps(value_list))

			'''新建入库单时生成单号，加载下拉框内容'''
		elif action == 'CreateStockInId':
			id = LoadStockInId()
			next_id = GetNextNumber(id)
			return HttpResponse(next_id)
		elif action == 'LoadGoodsName':
			value_list = getGoodsCombobox('goodsName')
			return HttpResponse(json.dumps(value_list))
		elif action == 'LoadGoodsCat':
			value_list = getGoodsCombobox('goodsCat')
			return HttpResponse(json.dumps(value_list))
		elif action == 'LoadSeller':
			value_list = getGoodsCombobox('seller')
			return HttpResponse(json.dumps(value_list))
		elif action == 'LoadManufactor':
			value_list = getGoodsCombobox('manufactor')
			return HttpResponse(json.dumps(value_list))
		elif action == 'LoadSupplier':
			value_list = getGoodsCombobox('supplier')
			return HttpResponse(json.dumps(value_list))
			'''保存新增的入库单'''
		elif action == 'Save':
			back = 0
			id = request.POST.get('stockIn_id')  #'000000003'    int(id)=3
			goods_id = request.POST.get('goods_id') #'1'
			cat = request.POST.get('cat')  #'1'
			rfid = request.POST.get('rfid')  #'S1233'
			amount = request.POST.get('amount') #'15'
			cost = request.POST.get('cost')   #'56'
			print(int(cost)/int(amount))
			#提交回来的是总的成本价，保存在数据库goodsInfo 中保存的是单价 ,stockIn中直接保存的总价
			exp_date = request.POST.get('exp_date')  #'05/13/2020'
			'''时间格式问题 前端dd/mm/yy 保存格式应是yy-mm-dd 暂时不知道怎么解决，先不添加时间数据'''

			seller = request.POST.get('seller')
			manufactor = request.POST.get('mfrs')
			supplier = request.POST.get('supplier')
			# 更新stockIn表   先添加主表数据
			In= models.StockIn.objects.create(stockin_id=id, goods_id=goods_id, cat_id=cat, goods_sn=rfid, in_amount=amount,
			                              cost=cost, performer_id=user_id, seller_id=seller, manufactor_id=manufactor,
			                              supplier_id=supplier)
			#更新goodsInfo表
			models.GoodsInfo.objects.create(stockin_id=In.id,goods_id=goods_id,cat_id=cat,goods_sn=rfid,goods_stock=amount,
			                                cost=int(cost)/int(amount),manufactor_id=manufactor,seller_id=seller,supplier_id=supplier)
			back = 1
			return HttpResponse(back)


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

'''
加载最大入库单编号 字符串形式，9位
若无数据返回的id为''
'''
def LoadStockInId():
	int_id = 1
	id = ''
	stock_Ins = models.StockIn.objects.all().order_by('-stockin_id')
	if stock_Ins.count() != 0:
		int_id = stock_Ins.first().stockin_id  #first是一个stockIn对象
		id = str(int_id).zfill(9)  #给字符串前面补零，保证9位长度
	return id

'''
生成下一个商品编号
BaseNumber 为字符串
'''
def GetNextNumber(BaseNumber):
	NewNumber = ""  #新值
	InNumber = 1    #进位
	PlaceValue = 0     #位值

	for num in BaseNumber[::-1]:
		if num == '9' and InNumber == 1:  #当前为9，并且需要进位
			InNumber = 1
			NewNumber = '0'+ NewNumber
		else:
			if InNumber == 1 and num >= '0' and num < '9': #需进位，但当前不是9，只需动当前这一位
				PlaceValue = int(num)
				PlaceValue = InNumber + PlaceValue   #  +1
				InNumber = 0     #进位结束
				NewNumber = str(PlaceValue) + NewNumber   #字符串拼接
			else:  #不需进位
				InNumber = 0
				NewNumber = num + NewNumber  #字符串拼接，注意顺序！

		if (BaseNumber == NewNumber):
			NewNumber = "0000000001"
	print(NewNumber)
	return NewNumber

'''加载商品下拉框'''
def getGoodsCombobox(select):
	querys = ''
	value_dict = {'id':'','name':''}
	value_list = []
	if select == "goodsName":
		querys = models.Goods.objects.all().extra({'id':'id','name':'goodsname'}).values('id','name')  #给字段起别名，必须写上values，不然并没有成功
	elif select == "goodsCat":
		querys = models.GoodsCat.objects.all().extra({'id':'id','name':'catname'}).values('id','name')  #给字段起别名，必须写上values，不然并没有成功
	elif select == "manufactor":
		querys = models.Manufactor.objects.all().extra({'id':'id','name':'name'}).values('id','name')  #给字段起别名，必须写上values，不然并没有成功
	elif select == "supplier":
		querys =models.Supplier.objects.all().extra({'id':'id','name':'name'}).values('id','name')  #给字段起别名，必须写上values，不然并没有成功
	elif select == "seller":
		querys = models.Seller.objects.all().extra({'id':'id','name':'Sellername'}).values('id','name')  #给字段起别名，必须写上values，不然并没有成功
	if querys.count != 0:
		for row in querys:
			value_dict['id'] = row['id']
			value_dict['name'] = row['name']
			value_list.append(value_dict.copy())
			value_dict.clear()
	return value_list