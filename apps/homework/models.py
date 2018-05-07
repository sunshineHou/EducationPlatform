#!/usr/bin/python3.6
# @Author : sunshine

"""作业模型层
"""

from django.db import models
from datetime import datetime

IS_BONUS = (  # 加分题选项
    ('1', '是'),
    ('0', '否'),
)

IS_DONE = IS_BONUS


class Assignment(models.Model):
    """作业布置类"""

    title = models.CharField(max_length=40, verbose_name='题目名称')
    class_name = models.CharField(max_length=20, verbose_name='班级')
    teacher = models.CharField(max_length=20, verbose_name='教师')
    course = models.CharField(max_length=20, verbose_name='课程')
    first_module = models.CharField(max_length=20, verbose_name='一级模块')
    second_module = models.CharField(max_length=30, verbose_name='二级模块')
    is_bonus = models.CharField(max_length=1, choices=IS_BONUS, default='0', verbose_name='加分题')
    refer_complete_time = models.CharField(max_length=5, default='10', verbose_name='参考完成时间(分钟数)')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        """Meta内部类"""
        verbose_name = '作业布置'
        verbose_name_plural = verbose_name

    def __repr__(self):
        return self.title

    __str__ = __repr__


# def set_homework_path(student, filename):
#     """设置学生作业的文件路径"""
#     return 'homework/%s/%s' % (student, filename)


class Submission(models.Model):
    """作业提交类"""
    student = models.CharField(max_length=20, verbose_name='学生')
    submit_answer = models.TextField(verbose_name='作业答案')
    title = models.CharField(max_length=40, verbose_name='题目名称')
    homework = models.FileField(upload_to='homework/%Y/%m/%d', verbose_name='上传作业')
    is_done = models.CharField(max_length=1, choices=IS_DONE,
                               default='0', verbose_name='完成')
    # complete_time = models.CharField(max_length=5, default='0', verbose_name='完成时间(分钟数)')
    created_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')

    class Meta:
        """Meta内部类"""
        verbose_name = '作业提交'
        verbose_name_plural = verbose_name

    def __repr__(self):
        return self.title

    __str__ = __repr__
