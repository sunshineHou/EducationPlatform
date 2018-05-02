#! /usr/bin/python3.6
# @Author : changshiqi

"""学生模型层
"""

from django.db import models

from classes.models import Class
from teachers.models import GENDERS

DEGREES = (  # 学历选项
    ('high school', '中专/高中'),
    ('undergraduate', '专科/本科'),
    ('master', '硕士研究生/硕士'),
)


class Student(models.Model):
    """学生类"""
    en_name = models.CharField(max_length=20, unique=True, verbose_name='英文名')
    passwd = models.CharField(max_length=200, verbose_name='密码')
    real_name = models.CharField(max_length=20, verbose_name='真实姓名')
    gender = models.CharField(max_length=6, choices=GENDERS, verbose_name='性别', default='male')
    degree = models.CharField(max_length=13, choices=DEGREES,
                              default='undergraduate', verbose_name='学历')
    mobile = models.CharField(max_length=11, verbose_name='手机号')
    height = models.CharField(verbose_name='身高', max_length=3)
    weight = models.CharField(verbose_name='体重', max_length=3)
    learning = models.CharField(max_length=200, verbose_name='学习经历')
    allergies = models.CharField(max_length=200, verbose_name='过敏史')
    class_name = models.ForeignKey(Class, null=True, blank=True, verbose_name='所属班级')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        """Meta内部类"""
        verbose_name = '学生'
        verbose_name_plural = verbose_name

    def __repr__(self):
        return self.en_name

    __str__ = __repr__
