# @author shi.qi.chang
from django import forms


class TchRegForm(forms.Form):
    """教师注册信息表单类"""

    name = forms.CharField(min_length=3, max_length=50)
    password = forms.CharField(min_length=6, max_length=200)


class TchLogForm(forms.Form):
    """教师登录信息表单类"""

    name = forms.CharField(min_length=3, max_length=50)
    password = forms.CharField(min_length=6, max_length=200)


class TchInfoForm(forms.Form):
    """教师基本信息表单类"""

    real_name = forms.CharField(min_length=2, max_length=50)
    gender = forms.CharField(required=True)
    degree = forms.CharField(required=True)
    major = forms.CharField(max_length=50, required=True)
    school = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)