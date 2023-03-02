from django.db import models

# Create your models here.

# 1.自己定义模型
# 密码需要加密，登录时还需要进行验证
# class User(models.Model):
#     username = models.CharField(max_length=20, unique=True)
#     password = models.CharField(max_length=20)
#     moblie = models.CharField(max_length=11, unique=True)


# 2.django自带的一个用户模型
# 这个用户模型 有密码的加密和验证
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    moblie = models.CharField(max_length=11, unique=True)

    class Meta:
        db_table = "tb_users"
        verbose_name = "用户管理"  # 单数形式
        verbose_name_plural = verbose_name  # 复数形式
