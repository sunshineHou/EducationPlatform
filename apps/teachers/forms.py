#! /usr/bin/python3.6
# @Author : sunshine

"""教师表单层
"""

import re
from django import forms
from django.core.exceptions import ValidationError
from students.forms import en_name_validate, real_name_validate
from teachers.models import TeacherUpload

def major_validate(value):
    """专业验证"""
    major_re = re.compile(r'^[\u4e00-\u9fa5]+$')
    if not major_re.match(value):
        raise ValidationError('仅支持中文字符')


school_validate = major_validate  # 学校验证


class TchRegForm(forms.Form):
    """教师注册信息表单类"""
    en_name = forms.CharField(validators=[en_name_validate, ], min_length=3, max_length=20)
    passwd = forms.CharField(min_length=6, max_length=200)


TchLogForm = TchRegForm  # 教师登录信息表单类


class TchInfoForm(forms.Form):
    """教师基本信息表单类"""
    en_name = forms.CharField(validators=[en_name_validate, ], min_length=3, max_length=20)
    passwd = forms.CharField(min_length=6, max_length=200)
    real_name = forms.CharField(validators=[real_name_validate, ], min_length=2, max_length=20)
    gender = forms.CharField(required=True)
    degree = forms.CharField(required=True)
    major = forms.CharField(validators=[major_validate, ], max_length=30, required=True)
    school = forms.CharField(validators=[school_validate, ], max_length=20, required=True)
    email = forms.EmailField(required=True)

class UploadForm(forms.ModelForm):
    class Meta:
        model = TeacherUpload
        fields = ['file']