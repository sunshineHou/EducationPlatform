#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author : sunshine

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, RequestContext
from django.views.generic import View
from .forms import StuRegForm, StuInfoForm, StuLogForm
from .models import Student
from django.contrib.auth.hashers import make_password, check_password
from homework.models import Assignment
from teachers.models import TeacherUpload


# Create your views here.
def homepage_stu(request):
    return render(request, 'home_page_stu.html')


class StuRegisterView(View):
    def get(self, request):
        return render(request, 'register_info_stu.html')

    def post(self, request):
        stu_reg_form = StuRegForm(request.POST)
        if stu_reg_form.is_valid():
            en_name = request.POST.get('en_name')
            passwd = request.POST.get('passwd')
            student = Student.objects.filter(en_name=en_name)
            print('*' * 50, en_name, passwd)
            if student:  # 用户名已存在
                return render(request, 'register_info_stu.html', {'msg': '用户名已存在'})
            return render(request, 'basic_info_stu.html', {'en_name': en_name,
                                                           'passwd': passwd})
        else:
            return render(request, 'register_info_stu.html', {'stu_reg_form': stu_reg_form})


class StuRegisterInfoView(View):
    def post(self, request):
        stu_info_form = StuInfoForm(request.POST)
        if stu_info_form.is_valid():
            en_name = request.POST.get('en_name')
            passwd = request.POST.get('passwd')
            real_name = request.POST.get('real_name')
            mobile = request.POST.get('mobile')
            gender = request.POST.get('gender')
            height = request.POST.get('height')
            weight = request.POST.get('weight')
            degree = request.POST.get('degree')
            learning = request.POST.get('learning')
            allergies = request.POST.get('allergies')

            student = Student()
            student.en_name = en_name
            student.passwd = make_password(passwd, 'dengguo', 'pbkdf2_sha256')
            student.real_name = real_name
            student.mobile = mobile
            student.gender = gender
            student.height = height
            student.weight = weight
            student.degree = degree
            student.learning = learning
            student.allergies = allergies
            student.save()
            return render(request, 'log_in_stu.html')
        else:
            return render(request, 'basic_info_stu.html', {'stu_info_form': stu_info_form})


class StuLoginView(View):
    def get(self, request):
        return render(request, 'log_in_stu.html')

    def post(self, request):
        stu_log_form = StuLogForm(request.POST)
        if stu_log_form.is_valid():
            en_name = request.POST.get('en_name')
            passwd = request.POST.get('passwd')
            students = Student.objects.filter(en_name=en_name)
            if students:
                for student in students:
                    result = check_password(passwd, student.passwd)
                    if result == 1:
                        request.session['student_id'] = student.id

                        stu_class = student.class_name
                        tasks = Assignment.objects.filter(class_name=stu_class)
                        print(tasks)
                        result_list = []
                        for task in tasks:
                            task_list = task.title
                            target_list = task_list.replace("['", '').replace("']", '').split("', '")
                            results = result_list.append(target_list)
                        all_info = {
                            'tasks': tasks,
                            'en_name': en_name,
                            # 'results': results,
                        }
                        return render(request, 'view_all_tasks_stu.html', all_info)
                else:
                    return render(request, 'log_in_stu.html', {'stu_log_form': stu_log_form})
            else:
                return render(request, 'register_info_stu.html', {})
        else:
            return render(request, 'log_in_stu.html', {'stu_log_form': stu_log_form})



@login_required
def logout_stu(request):
    try:
        del request.session['student_id']
    except KeyError as e:
        print(e)
    return render(request, 'log_in_stu.html')


@login_required
def view_course_ware(request):
    files = TeacherUpload.objects.all()
    return render(request, 'view_course_ware.html', {'files': files})
