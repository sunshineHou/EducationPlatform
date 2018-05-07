#! /usr/bin/python3.6
# @Author : sunshine

"""班级模型层
"""

from django.db import models
from django.contrib.auth.models import User


class Class(models.Model):
    """班级类"""
    name = models.CharField(max_length=20, unique=True, verbose_name='班级名称')
    major = models.CharField(max_length=20, verbose_name='班级专业')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    modified_time = models.DateTimeField(auto_now=True, verbose_name='最后一次修改时间')
    administrator = models.ForeignKey(User, related_name='+', verbose_name='管理员')

    class Meta:
        """Meta内部类"""
        verbose_name = '班级'
        verbose_name_plural = verbose_name

    def get_all_students(self):
        return self.student_set.all()

    def __repr__(self):
        return self.name

    __str__ = __repr__
