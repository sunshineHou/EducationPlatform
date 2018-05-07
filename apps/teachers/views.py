#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author : sunshine

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse
from django.views.generic import View
from .forms import TchRegForm, TchInfoForm, TchLogForm, UploadForm
from .models import Teacher
from django.contrib.auth.hashers import make_password, check_password
from knowledgequestions.models import Course
from classes.models import Class
from knowledgequestions.models import Module, KnowledgeBase, QuestionBank


# Create your views here.
def homepage_tch(request):
    return render(request, 'home_page_tea.html')


class TchRegisterView(View):
    def get(self, request):
        return render(request, 'register_info_tea.html', {})

    def post(self, request):
        tch_reg_form = TchRegForm(request.POST)
        if tch_reg_form.is_valid():
            en_name = request.POST.get('en_name')
            passwd = request.POST.get('passwd')
            # print(en_name, passwd, '*' * 50)
            teacher = Teacher.objects.filter(en_name__exact=en_name)
            # print(teacher, '&' * 100)
            if teacher:  # 用户名已存在
                return render(request, 'register_info_tea.html', {'msg': '用户名已存在'})
            return render(request, 'basic_info_tea.html', {'en_name': en_name,
                                                           'passwd': passwd})
        else:
            return render(request, 'register_info_tea.html', {'tch_reg_form': tch_reg_form})


class TchRegisterInfoView(View):
    def post(self, request):
        tch_info_form = TchInfoForm(request.POST)
        if tch_info_form.is_valid():
            en_name = request.POST.get('en_name')
            passwd = request.POST.get('passwd')
            real_name = request.POST.get('real_name')
            gender = request.POST.get('gender')
            degree = request.POST.get('degree')
            school = request.POST.get('school')
            major = request.POST.get('major')
            email = request.POST.get('email')

            teacher = Teacher()
            teacher.en_name = en_name
            teacher.passwd = make_password(passwd, 'dengguo', 'pbkdf2_sha256')
            teacher.real_name = real_name
            teacher.school = school
            teacher.gender = gender
            teacher.degree = degree
            teacher.major = major
            teacher.email = email
            teacher.save()
            return render(request, 'log_in_tea.html')
        else:
            return render(request, 'basic_info_tea.html', {'tch_info_form': tch_info_form})


class TchLoginView(View):
    def get(self, request):
        return render(request, 'log_in_tea.html', {})

    def post(self, request):
        tch_log_form = TchLogForm(request.POST)
        if tch_log_form.is_valid():
            en_name = tch_log_form.cleaned_data['en_name']
            passwd = tch_log_form.cleaned_data['passwd']
            teachers = Teacher.objects.filter(en_name=en_name)
            if teachers:
                for teacher in teachers:
                    result = check_password(passwd, teacher.passwd)
                    # print(result)
                    if result == 1:
                        request.session['teacher_id'] = teacher.id

                        classes = Class.objects.all()
                        courses = Course.objects.all()
                        info = {
                            'classes': classes,
                            'courses': courses,
                            'en_name': en_name,
                        }
                        return render(request, 'publish_tasks.html', info)
                    else:
                        return render(request, 'log_in_tea.html', {'tch_log_form': tch_log_form})
            else:
                return render(request, 'register_info_tea.html')
        else:
            return render(request, 'log_in_tea.html', {'tch_log_form': tch_log_form})


@login_required
def logout_tch(request):
    try:
        del request.session['teacher_id']
    except KeyError as e:
        print(e)
    return render(request, 'home_page_tea.html')


class UploadView(View):
    def get(self, request):
        classes = Class.objects.all()
        return render(request, 'upload.html', {'classes': classes})

    def post(self, request):
        uploadform = UploadForm(request.POST, request.FILES)
        if uploadform.is_valid():
            to_class = request.POST.get('to_class', '')
            class_obj = Class.objects.get(name=to_class)
            upload_obj = uploadform.save(commit=False)
            upload_obj.to_class = class_obj
            upload_obj.save()
            return self.get(request)
        else:
            return HttpResponse('上传失败')
