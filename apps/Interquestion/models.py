#!/usr/bin/python3.6
# _*_ coding: utf-8 _*_
# @Author: sunshine
# @Time: 18-1-27 下午4:42
# @Software: PyCharm

"""面试题库模型层
"""

from django.db import models
from django.contrib.auth.models import User

from homework.models import IS_BONUS

IS_DELETE = IS_BONUS  # 作业完成选项和删除选项

IS_RIGHT = (  # 作业对错选项
    ('1', '对'),
    ('0', '错'),
)

IS_DONE = (  # 作业对错选项
    ('1', '已完成'),
    ('0', '未完成'),
)

CATEGORIES = (  # 面试题目分类选项
    ('python', 'Python知识性题目'),
    ('algorithms', '算法题目'),
)


class InterviewCategory(models.Model):
    """面试题目分类表"""
    category = models.CharField(max_length=10, default='python',
                                choices=CATEGORIES, verbose_name='题目分类')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        """Meta内部类"""
        verbose_name = '面试题目分类'
        verbose_name_plural = verbose_name

    def __repr__(self):
        return self.category

    __str__ = __repr__


class InterviewQuestionBank(models.Model):
    """面试题库类"""
    title = models.CharField(max_length=100, verbose_name='题目名称')
    content = models.CharField(max_length=500, verbose_name='题目内容')
    category = models.ForeignKey(InterviewCategory, default='python', verbose_name='题目分类')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    modified_time = models.DateTimeField(auto_now=True, verbose_name='最后一次修改时间')
    creator = models.ForeignKey(User, related_name='+', verbose_name='创建者')
    modifier = models.ForeignKey(User, related_name='+', null=True, blank=True, verbose_name='修改者')

    class Meta:
        """Meta内部类"""
        verbose_name = '面试题库'
        verbose_name_plural = verbose_name

    def __repr__(self):
        return self.title

    __str__ = __repr__


class InterviewAssignment(models.Model):
    """面试作业布置类"""
    # times = models.CharField(max_length=5, verbose_name='布置次数')
    title = models.CharField(max_length=100, verbose_name='题目名称')
    class_name = models.CharField(max_length=20, verbose_name='班级')
    teacher = models.CharField(max_length=20, verbose_name='教师')
    category = models.CharField(max_length=10, verbose_name='题目分类')
    refer_complete_time = models.CharField(max_length=5, default='10', verbose_name='参考完成时间(分钟数)')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        """Meta内部类"""
        verbose_name = '面试作业布置'
        verbose_name_plural = verbose_name

    def __repr__(self):
        return self.title

    __str__ = __repr__


# def set_interview_path(student, filename):
#     """设置学生面试作业的文件路径"""
#     return 'interview/%s/%s' % (student, filename)


class InterviewSubmission(models.Model):
    """面试作业提交类"""
    # times = models.ForeignKey(InterviewAssignment, null=True, blank=True, verbose_name='布置次数')
    student = models.CharField(max_length=20, verbose_name='学生')
    submit_answer = models.TextField(verbose_name='作业答案')
    title = models.CharField(max_length=100, verbose_name='题目名称')
    is_done = models.CharField(max_length=1, default='0', choices=IS_DONE, verbose_name='完成度')
    complete_time = models.CharField(max_length=5, default='10', verbose_name='完成时间(分钟数)')
    is_delete = models.CharField(max_length=1, default='0', choices=IS_DELETE, verbose_name='删除')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        """Meta内部类"""
        verbose_name = '面试作业提交'
        verbose_name_plural = verbose_name

    def __repr__(self):
        return self.submit_answer

    __str__ = __repr__


class InterviewCorrecting(models.Model):
    """面试作业批改类"""
    student = models.CharField(max_length=20, verbose_name='学生')
    # times = models.ForeignKey(InterviewAssignment, null=True, blank=True, verbose_name='布置次数')
    question_answer = models.TextField(verbose_name='题目答案')
    title = models.CharField(max_length=100, verbose_name='题目名称')
    is_right = models.CharField(max_length=1, default='0', choices=IS_RIGHT, verbose_name='答案对错')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        """Meta内部类"""
        verbose_name = '面试作业批改'
        verbose_name_plural = verbose_name

    def __repr__(self):
        return self.question_answer

    __str__ = __repr__
