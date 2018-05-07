#! /usr/bin/python3.6
# @Author : sunshine

"""学生表单层
"""

import re

from django import forms
from django.core.exceptions import ValidationError


def en_name_validate(value):
    """英文名验证"""
    en_name_re = re.compile(r'^[a-zA-Z]{3,}$')
    if not en_name_re.match(value):
        raise ValidationError('仅支持英文字母，不区分大小写')


def real_name_validate(value):
    """真实姓名验证"""
    real_name_re = re.compile(r'^[\u4e00-\u9fa5·]{2,}$')
    if not real_name_re.match(value):
        raise ValidationError('仅支持中文字符和.符号')


def mobile_validate(value):
    """手机号码验证"""
    mobile_re = re.compile(r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$')
    if not mobile_re.match(value):
        raise ValidationError('手机号码格式错误')


def height_validate(value):
    """身高验证"""
    height_re = re.compile(r'^[0-9]+$')
    if not height_re.match(value):
        raise ValidationError('仅支持数字')


weight_validate = height_validate  # 体重验证


class StuRegForm(forms.Form):
    """学生注册信息表单类"""
    en_name = forms.CharField(validators=[en_name_validate, ], min_length=3, max_length=20)
    passwd = forms.CharField(min_length=6, max_length=200)


StuLogForm = StuRegForm  # 学生登录信息表单类


class StuInfoForm(forms.Form):
    """学生基本信息表单类"""
    en_name = forms.CharField(validators=[en_name_validate, ], min_length=3, max_length=20)
    passwd = forms.CharField(min_length=6, max_length=200)
    real_name = forms.CharField(min_length=2, max_length=20)
    mobile = forms.CharField(validators=[mobile_validate, ])
    gender = forms.CharField(required=True)
    height = forms.CharField(required=True, validators=[height_validate, ])
    weight = forms.CharField(required=True, validators=[weight_validate, ])
    degree = forms.CharField(required=True)
    learning = forms.CharField(max_length=200, min_length=1)
    allergies = forms.CharField(max_length=200, min_length=1)
