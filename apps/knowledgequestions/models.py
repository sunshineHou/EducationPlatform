#!/usr/bin/python3.6
# @Author : changshiqi

"""知识库和题库模型层
"""

from django.db import models
from django.contrib.auth.models import User


DIFFICULTY_LEVELS = (  # 难易程度选项
    ('beginner', '初级'),
    ('intermediate', '中级'),
    ('advanced', '高级'),
)


class Course(models.Model):
    """课程类"""
    name = models.CharField(max_length=20, unique=True, verbose_name='课程名字')
    detail = models.CharField(max_length=100, blank=True, verbose_name='课程详情')
    difficulty_level = models.CharField(max_length=10, choices=DIFFICULTY_LEVELS,
                                        default='beginner', verbose_name='难易程度')
    category = models.CharField(max_length=20, default='后端', verbose_name='课程类型')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    modified_time = models.DateTimeField(auto_now=True, verbose_name='最后一次修改时间')
    creator = models.ForeignKey(User, related_name='+', verbose_name='创建者')
    modifier = models.ForeignKey(User, related_name='+', null=True, blank=True, verbose_name='修改者')

    class Meta:
        """Meta内部类"""
        verbose_name = '课程'
        verbose_name_plural = verbose_name

    def __repr__(self):
        return self.name

    __str__ = __repr__


class Module(models.Model):
    """知识模块类"""
    course = models.ForeignKey(Course, verbose_name='课程')
    name = models.CharField(max_length=20, verbose_name='模块名称')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    modified_time = models.DateTimeField(auto_now=True, verbose_name='最后一次修改时间')
    creator = models.ForeignKey(User, related_name='+', verbose_name='创建者')
    modifier = models.ForeignKey(User, related_name='+', null=True, blank=True, verbose_name='修改者')

    class Meta:
        """Meta内部类"""
        verbose_name = '知识模块'
        verbose_name_plural = verbose_name

    def __repr__(self):
        return self.name

    def get_knowledgebase(self):
        """获取所有的二级模块"""
        return self.knowledgebase_set.all()

    __str__ = __repr__


class KnowledgeBase(models.Model):
    """知识库类"""
    module = models.ForeignKey(Module, verbose_name='知识模块')
    name = models.CharField(max_length=30, verbose_name='二级模块')
    knowledge_point = models.CharField(max_length=50, blank=True, verbose_name='知识点')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    modified_time = models.DateTimeField(auto_now=True, verbose_name='最后一次修改时间')
    creator = models.ForeignKey(User, related_name='+', verbose_name='创建者')
    modifier = models.ForeignKey(User, related_name='+', null=True, blank=True, verbose_name='修改者')

    class Meta:
        """Meta内部类"""
        verbose_name = '知识库'
        verbose_name_plural = verbose_name

    def __repr__(self):
        return self.name

    __str__ = __repr__


class QuestionBank(models.Model):
    """题库类"""
    title = models.CharField(max_length=20, verbose_name='题目名称')
    content = models.CharField(max_length=500, verbose_name='题目内容')
    difficulty_level = models.CharField(max_length=10, choices=DIFFICULTY_LEVELS,
                                        default='beginner', verbose_name='难易程度')
    knowledgebase = models.ForeignKey(KnowledgeBase, default='', verbose_name='二级模块')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    modified_time = models.DateTimeField(auto_now=True, verbose_name='最后一次修改时间')
    creator = models.ForeignKey(User, related_name='+', verbose_name='创建者')
    modifier = models.ForeignKey(User, related_name='+', null=True, blank=True, verbose_name='修改者')

    class Meta:
        """Meta内部类"""
        verbose_name = '题库'
        verbose_name_plural = verbose_name

    def __repr__(self):
        return self.title

    __str__ = __repr__
