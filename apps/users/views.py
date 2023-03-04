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
import re

from django.http import JsonResponse

from django.views import View
from apps.users.models import User


class UsernameCountView(View):
    
    def get(self, request, username):
        # 1. 接收用户名, 对用户名进行判断
        if not re.match('[a-zA-Z0-9_-]{5,20}', username):
              return JsonResponse({'code': 0, 'errmsg': "用户名不满足需求"})
        # 2. 数据库查询
        count = User.objects.filter(username=username).count()
        # 3. 返回响应
        return JsonResponse({'code': 0, 'count': count, 'errmsg': 'ok'})



"""
注册功能

前端： 当用户输入用户名、密码、确认密码、手机号、验证码、是否同意协议, 点击注册按钮，会发送一个axios请求

后端： 请求             接收请求 获取数据
       逻辑判断         验证数据 保存到数据库
       响应             json   {code: 0, errmsg: ok}

路由： POST   regsiter/
       
步骤： 1. 接收请求
       2. 获取数据
       3. 验证数据
       4. 数据入库
       5. 返回响应
"""

import json

class RegisterView(View):
     
     def post(self, request):
          # 1. 接收请求(POST json)
          body_bytes = request.body
          body_str = body_bytes.decode()
          body_dict = json.loads(body_str)
          # 2. 获取数据
          username = body_dict.get("username")
          password = body_dict.get('password')
          password2 = body_dict.get('password2')
          mobile = body_dict.get('moblie')
          allow = body_dict.get('allow')
          # 3. 验证数据
          # 3.1 用户名、密码、确认密码、手机号、验证码、是否同意协议 都要有
          if not all([username, password, password2, mobile]):
              return JsonResponse({"code": 400, "errmsg": "参数不全"}) 
          # 3.2 验证用户名不可以重复
          if not re.match('[a-zA-Z0-9_-]{5,20}', username):
              return JsonResponse({"code": 400, "errmsg": "用户名不符合规则"})
          # 3.3 验证密码满足规则
          # 3.4 确认密码和密码要一致
       #    if password != password2:
       #         return JsonResponse({"code": 400, "errmsg": "密码不一致"})
       #    # 3.5 手机号要满足规则 手机号不能重复
       #    obj = User.objects.filter(moblie=mobile)
       #    if obj:
       #         return JsonResponse({"code": 400, "errmsg": "该手机号已被注册"})
       #    # 3.6 需要同意协议
       #    if not allow:
       #         return JsonResponse({"code": 400, "errmsg": "请同意协议"})
          # 4. 数据入库
          # 方式一
       #    user = User(username=username, password=password, moblie=moblie)
       #    user.save()
          # 方式二
       #    User.objects.create(us1       qwername=username, password=password, moblie=moblie)
          # 密码没有加密的解决方法
          User.objects.create_user(username=username, password=password, moblie=mobile)
          # 5. 返回响应
          return JsonResponse({"code": 0, "errmsg": "ok"})
