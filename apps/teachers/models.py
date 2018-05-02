#! /usr/bin/python3.6
# @Author : changshiqi

"""教师模型层
"""

from django.db import models
from classes.models import Class
from datetime import datetime

GENDERS = (  # 性别选项
    ('male', '男'),
    ('female', '女'),
)

DEGREES = (  # 学历选项
    ('undergraduate', '本科'),
    ('master', '硕士'),
    ('doctor', '博士'),
)


class Teacher(models.Model):
    """教师类"""
    en_name = models.CharField(max_length=20, unique=True, verbose_name='英文名')
    passwd = models.CharField(max_length=200, verbose_name='密码')
    real_name = models.CharField(max_length=20, verbose_name='真实姓名')
    gender = models.CharField(max_length=6, choices=GENDERS, verbose_name='性别', default='male')
    degree = models.CharField(max_length=15, choices=DEGREES,
                              default='undergraduate', verbose_name='学历')
    major = models.CharField(max_length=30, verbose_name='专业')
    school = models.CharField(max_length=20, verbose_name='学校')
    email = models.EmailField(verbose_name='邮箱')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        """Meta内部类"""
        verbose_name = '教师管理'
        verbose_name_plural = verbose_name

    def __repr__(self):
        return self.en_name

    __str__ = __repr__


class ClassTeacher(models.Model):
    """班级教师类，用于关联班级模型和教师模型"""
    class_name = models.ForeignKey(Class, verbose_name='班级')
    teacher = models.ForeignKey(Teacher, verbose_name='教师')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        """Meta内部类"""
        verbose_name = '关联班级和教师'
        verbose_name_plural = verbose_name

    def __repr__(self):
        return '%s:%s' % (self.class_name, self.teacher)

    __str__ = __repr__


class TeacherUpload(models.Model):
    file = models.FileField(upload_to='teachers_upload/%Y/%m/%d', verbose_name='上传文件')
    to_class = models.ForeignKey(Class, verbose_name='班级')
    pub_time = models.DateTimeField(default=datetime.now, verbose_name='发布时间')

    class Meta:
        """Meta内部类"""
        verbose_name = '上传课件'
        verbose_name_plural = verbose_name


