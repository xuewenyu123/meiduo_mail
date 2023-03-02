from django.shortcuts import render

# Create your views here.

"""
需求分析：根据页面上的功能（从上到下，从左到右）, 看哪些功能需要和后端配合
如何确定 那些功能需要和后端进行交互呢？
        1.经验
        2.关注相似网站的相似功能

"""


"""
判断用户名是否重名的功能

前端： 当用户输入用户名之后，失去焦点，会发送一个ajax请求

后端： 请求             接收用户名
       逻辑判断         根据用户名去数据库查询 如果count = 1 说明该用户名已经被注册了
                        如果count = 0 说明用户名没有被注册
       响应             json   {code: 0, count: 0/1, errmsg: ok}

路由： GET   usernames/<username>/count/
       
步骤： 1. 接收用户名
       2. 数据库查询
       3. 返回响应
"""

from django.http import JsonResponse

from django.views import View
from apps.users.models import User


class UsernameCountView(View):
    
    def get(self, request, username):
        # 1. 接收用户名
        # 2. 数据库查询
        count = User.objects.filter(username=username).count()
        # 3. 返回响应
        return JsonResponse({'code': 0, 'count': count, 'errmsg': 'ok'})
