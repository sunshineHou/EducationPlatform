#! /usr/bin/python3.6
# @Author : sunshine

"""作业表单层
"""

from django import forms
from .models import Submission


class AssignmentsForm(forms.Form):
    """作业布置表单类"""
    class_name = forms.CharField(required=True)
    course = forms.CharField(required=True)
    first_module = forms.CharField(required=True)
    second_module = forms.CharField(required=True)
    # refer_complete_time = forms.CharField(required=True)
    # is_bonus = forms.CharField(required=True)
    is_release = forms.CharField(required=True)


class CompletionForm(forms.Form):
    """作业完成度表单类"""
    class_name = forms.CharField(required=True)
    course = forms.CharField(required=True)
    created_time = forms.CharField(required=True)


class FileForm(forms.ModelForm):
    """文件上传表单类"""
    class Meta:
        model = Submission
        fields = ['homework']
