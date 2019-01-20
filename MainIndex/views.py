from django.shortcuts import render
from django.http import HttpResponse
from Models import models
import json


def frame(request):# request  接收的请求
    # return HttpResponse('hello world')  #返回字符串
    action = request.POST.get('action')

    if request.method == 'GET':
        return render(request, 'MainIndex/main.html')  ##用render，从第二个参数中找
    else:
        if action=='Loadsy':
            return HttpResponse('/home/')
        elif action=='LoadFirstMenuByPermis':
            #user_id=request.session.get("Login_UserId")
            # request.session[‘Login_UserId’]=id
            user_id=request.session.get("Login_UserId")    #注意小括号！！

            # 1、根据role_id得到角色权限菜单权限列表
            # obj= models.User.objects.filter(user_id=user_id).first()
            # roles=obj.roles.all()
            # for role in roles:
            #     role_id=role.role_id
            roles_id=models.User.objects.filter(user_id=user_id).values('user_role__role__role_id')# 一个字典  #根据user_id 获取role_id
            user_role_menu_get=[]
            for role_id in roles_id:
                roles=models.Role.objects.get(role_id=role_id['user_role__role__role_id']) #根据id只会有一条数据
                #if roles.count():
                menus=roles.permissions.filter(menu_show=1)
                for menu in menus:
                    user_role_menu_get.append(menu.menu_id)#将菜单名添加进列表
            # 2、根据user_id，查出其所有用户权限所拥有的菜单列表
            users=models.User.objects.get(user_id=user_id)
            #if users.count():
            menus=users.menus.filter(menu_show=1)
            for menu in menus:
                user_role_menu_get.append(menu.menu_id)
            user_role_menu = list(set(user_role_menu_get))  # 去重
            user_role_menu.sort(key=user_role_menu_get.index)  # 按原来排序，此时将user对应的所有的role的角色权限菜单已全部以列表形式获取
            menu_dict = {'menu_id': '', 'menu_name': '', 'menu_describe': '', 'menu_url': '', 'menu_img': '',
                    'menu_show': '', 'menu_open': '', 'menu_node': '', }  # 用字典和列表拼接很方便形成Json格式
            menu=[]
            for menu_id in user_role_menu:
                menu_qs=models.Menu.objects.filter(menu_id=menu_id)
                for row in menu_qs:
                    menu_dict['menu_id'] = row.menu_id
                    menu_dict['menu_name'] = row.menu_name
                    menu_dict['menu_describe'] = row.menu_describe
                    menu_dict['menu_url'] = row.menu_url
                    menu_dict['menu_img'] = row.menu_img
                    menu_dict['menu_show'] = row.menu_show
                    menu_dict['menu_open'] = row.menu_open
                    menu_dict['menu_node'] = row.menu_node
                    menu.append(menu_dict.copy())# 直接使用append方法将字典添加到列表中，如果需要更改字典中的数据，那么列表中的内容也会发生改变
            #     # 用.copy()就不会跟着改变
            menu.sort(key=lambda x: x['menu_node']) #lambda是一个匿名函数，是固定写法，不要写成别的单词；
            # x表示列表中的一个元素，在这里，表示一个字典，x只是临时起的一个名字，你可以使用任意的名字；
            # x['node']表示字典里的node键，所以这句命令的意思就是按照列表中node键排序
            request.session["AllMenuInfoByUserId"] = menu
            menuJSON = json.dumps(menu)  # 将列表转字符串传给前端
            return HttpResponse(menuJSON)
        elif action=='LoadSecondMenu':
            ParentNode = request.POST.get('ParentNode')  #前端foreach每一次获得的一个顶级节点，是字符串
            wholemenus = request.session.get('AllMenuInfoByUserId') #[{}]
            getsecondmenu = GetSecondMenu(ParentNode,wholemenus)
            secondmenu=json.dumps(getsecondmenu)
            return HttpResponse(secondmenu)
        elif action=='JudgeOverTime':
            isovertime = 0
            if (request.session.get("Login_UserId") == None):
                isovertime = 1
        return HttpResponse(isovertime)


#根据给的父节点在整个菜单结点中找到下级子结点
def GetSecondMenu(parentNode,wholeMenues):
    menujson=[]
    for menu in wholeMenues:
        #menu  {'menu_id': 3, 'menu_name': '商品类型配置', 'menu_describe': None, 'menu_url': '/goodsCat/', 'menu_img': 'emotion_happy.png', 'menu_show': 1, 'menu_open': None, 'menu_node': '10001003'}
        if len(menu['menu_node']) == len(parentNode)+4 and parentNode == menu['menu_node'][0:len(parentNode)]:
            menujson.append(menu)
#[{'menu_id': 2, 'menu_name': '商品信息配置', 'menu_describe': None, 'menu_url': '/goods/', 'menu_img': 'emotion_happy.png', 'menu_show': 1, 'menu_open': None, 'menu_node': '10001002'},
# {'menu_id': 3, 'menu_name': '商品类型配置', 'menu_describe': None, 'menu_url': '/goodsCat/', 'menu_img': 'emotion_happy.png', 'menu_show': 1, 'menu_open': None, 'menu_node': '10001003'}]
    return menujson



def home(request):
    return render(request,'MainIndex/home.html')

