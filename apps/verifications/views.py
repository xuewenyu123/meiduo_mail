from django.shortcuts import render
from django.views import View


"""
前端：  拼接一个url 然后给img  img会发送请求
        url = http://ip:port/image_codes/uuid/

后端：  
        请求        接收路由中的uuid
        业务逻辑    生成图片验证码和图片二进制  通过redis把图片验证码保存起来
        响应        返回图片二进制

        路由：      GET  image_codes/uuid/
        步骤：      1.接收路由中的 uuid
                    2.生成图片验证码和图片二进制
                    3.通过redis把图片验证码保存起来
                    4.返回图片二进制
"""

class ImageCodeView(View):

    def get(self, request, uuid):
        pass
