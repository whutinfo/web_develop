from django.shortcuts import render,redirect,render_to_response
from django.http import HttpResponse,HttpResponseRedirect

from django.views.decorators.csrf import csrf_exempt
from . import models


# 每个响应对应一个函数，函数必须返回一个响应
# 函数必须存在一个参数，一般约定为request
# 每个响应函数对应一个url


###ajax提交页面不刷新
# 在用对话框的时候一般用ajax,对话框一般在少量输入的时候使用
#用表单提交,url跳转方式  用于对大量的数据以及操作，比如博客这种

def login(request):
    '''
    处理用户请求，并返回内容
    :param request: 用户请求相关的所有信息（对象）
    :return:
    '''
    # return HttpResponse('hello world')
    #用判断请求方式来执行不同的命令
    if request.method=='GET':
        print('login')
        return render(request, 'login/login.html')#自动找到模板路径下的login.html文件，读取内容并返回给用户
    else:
        print('login的post')
        user_name = request.POST.get('Account')
        user_pwd = request.POST.get('Pwd')
        if (user_name == '管理员') & (user_pwd == '123'):
            # print('提交')   这种会在下面的运行里进行打印，平时测试方便
            return HttpResponse(3)
            # 表单形式提交才可以用重定向这种方式直接跳转url
            # ajax用redirect是没有用的，只能返回字符串，所以需要在html中用location.href的方式写跳转
        else:
            print('2')
            return HttpResponse(0)


####以表单形式提交，redirect重定向跳转
## 表单形式一定会刷新一次页面，所以需要ajax，不改变这个页面的显示下传值过来
def login1(request):
    if request.method == 'GET':
        print('login1')
        return render(request, 'login/login.html')  # 自动找到模板路径下的login.html文件，读取内容并返回给用户
    else:
        print('login1的post')
        user_name = request.POST.get('account')
        user_pwd = request.POST.get('pwd')

        if (user_name == '管理员') & (user_pwd == '123'):
            # print('提交')   这种会在下面的运行里进行打印，平时测试方便
            return redirect('/mainIndex/')
            # 表单形式提交才可以用重定向这种方式直接跳转url
            # ajax用redirect是没有用的，只能返回字符串，所以需要在html中用location.href的方式写跳转
        else:
            print('2')
            return redirect('/login1/')


def index(request):
    #增加
   # models.UserGroup.objects.create(title='销售部')
   # models.UserInfo.objects.create(user='root',password='pwd',age=12,ug_id=1)

    #查询
    group_list=models.UserGroup.objects.all()  # 拿所有数据
    #group_title=models.UserGroup.objects.all().values('title')#只取title一列
    #group_list.QuerySet类型（列表）
    print(group_list)
    for row in group_list:
        print(row.id,row.title)

    group_filter=models.UserGroup.objects.filter(id=1,title='销售部')  #带条件过滤
    #group1=models.UserGroup.objects.filter(id__gt=1) #__gt  大于  __lt 小于
    for row in group_filter:
        print(row.id,row.title)

    #删除
    #models.UserGroup.objects.filter(id=2).delete()

    #更新
    models.UserGroup.objects.filter(id=2).update(title='公关部')

    return HttpResponse('123')


def test(request):
    #创建数据
    '''
    models.UserType.objects.create(title='普通用户')
    models.UserType.objects.create(title='二逼用户')
    models.UserType.objects.create(title='牛逼用户')

    models.UserInfo.objects.create(name='方绍伟',age=19,ut_id=1)
    models.UserInfo.objects.create(name='尤庆斌',age=18,ut_id=2)
    models.UserInfo.objects.create(name='刘庚',age=15,ut_id=2)
    models.UserInfo.objects.create(name='陈涛',age=19,ut_id=3)
    models.UserInfo.objects.create(name='王者',age=19,ut_id=3)
    models.UserInfo.objects.create(name='杨涵',age=19,ut_id=1)
    '''

    result=models.UserInfo.objects.filter(name='王者')
    for obj in result:
        print(obj.name,obj.age,obj.ut_id)
        print(obj.ut.title)
    return HttpResponse('test')
