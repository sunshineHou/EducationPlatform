#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author : dengguo

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect
from .models import Submission, Assignment
from django.views.generic import View, ListView
from knowledgequestions.models import Course
from classes.models import Class
from knowledgequestions.models import Module, KnowledgeBase, QuestionBank
import json
from .forms import AssignmentsForm, FileForm
from teachers.models import Teacher
from students.models import Student
from django.core.urlresolvers import reverse


# Create your views here.
@login_required
def get_tch_session(request):
    teacher_id = request.session['teacher_id']
    if teacher_id:
        teachers = Teacher.objects.filter(id=teacher_id)
        for teacher in teachers:
            en_name = teacher.en_name
            return en_name


@login_required
def get_stu_session(request):
    student_id = request.session['student_id']
    if student_id:
        students = Teacher.objects.filter(id=student_id)
        for student in students:
            en_name = student.en_name
            return en_name


class PublishView(View):
    def get(self, request):
        course_name = request.GET.get('q')
        course = Course.objects.filter(name=course_name)
        modules = Module.objects.filter(course=course)
        module_dict = {}
        for module in modules:
            module_name = module.name
            module_dict['%s' % module_name] = module_name
        return HttpResponse(json.dumps(module_dict), content_type="application/json")


@login_required
def submit_module_info(request):
    if request.method == 'GET':
        module_name = request.GET.get('q')
        module = Module.objects.filter(name=module_name)
        knowledgebases = KnowledgeBase.objects.filter(module=module)
        knowledgebase_dict = {}
        for knowledgebase in knowledgebases:
            knowledgebase_name = knowledgebase.name
            knowledgebase_dict['%s' % knowledgebase_name] = knowledgebase_name
        return HttpResponse(json.dumps(knowledgebase_dict), content_type="application/json")


@login_required
def submit_knowledgebase_info(request):
    if request.method == 'GET':
        knowledgebase_name = request.GET.get('q')
        knowledgebase = KnowledgeBase.objects.filter(name=knowledgebase_name)
        questionbanks = QuestionBank.objects.filter(knowledgebase=knowledgebase)
        questionbank__dict = {}
        for questionbank in questionbanks:
            questionbank_title = questionbank.title
            questionbank__dict['%s' % questionbank_title] = questionbank_title
        return HttpResponse(json.dumps(questionbank__dict), content_type="application/json")


@login_required
def submit_tasks_info(request):
    assignmentsForm = AssignmentsForm(request.POST)
    print('hello world!')
    if assignmentsForm.is_valid():
        class_name = request.POST.get('class_name')
        course = request.POST.get('course')
        first_module = request.POST.get('first_module')
        second_module = request.POST.get('second_module')
        question_title = request.POST.getlist('is_release')

        assignment = Assignment()
        assignment.class_name = class_name
        assignment.title = question_title
        assignment.teacher = get_tch_session(request)
        assignment.course = course
        assignment.first_module = first_module
        assignment.second_module = second_module
        assignment.save()

        classes = Class.objects.all()
        courses = Course.objects.all()
        info = {
            'classes': classes,
            'courses': courses,
            'en_name': get_tch_session(request)
        }
        return render(request, 'publish_tasks.html', info)
    else:
        return render(request, 'publish_tasks.html', {'assignmentsForm': assignmentsForm})


class ViewTheDegreeOfCompletionView(View):
    def get(self, request):
        en_name = get_stu_session(request)
        students = Student.objects.filter(en_name=en_name)
        for student in students:
            stu_class = student.class_name
            tasks = Assignment.objects.filter(class_name=stu_class)
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
            return render(request, 'view_the_degree_of_completion_tch.html', all_info)

    def post(self, request):
        pass

class SubmitView(View):
    def get(self, request):
        create_time = request.GET.get('create_time')
        course = request.GET.get('course')
        all_info = request.GET.get('all_info')

        student_id = get_stu_session(request)
        print(type(student_id))
        print(student_id)
        students = Student.objects.filter(en_name=student_id)
        for student in students:
            stu_class = student.class_name
            assignments = Assignment.objects.filter(course=course, class_name=stu_class)
            for assignment in assignments:
                title_list = assignment.title
                title_list = title_list.replace("['", '').replace("']", '').split("', '")
                print(title_list)
                print(type(title_list))
                question_list = []
                for title in list(title_list):
                    questions = QuestionBank.objects.filter(title=title)
                    for question in questions:
                        question_list.append(question)
                info = {
                    'question_list': question_list,
                    'en_name': get_stu_session(request),
                    'all_info': all_info,
                    'create_time': create_time,
                    'course': course
                }
                return render(request, 'detail_of_task.html', info)

    def post(self, request):
        student_info = {'en_name': get_stu_session(request)}
        fileform = FileForm(request.POST, request.FILES)
        if fileform.is_valid():
            file_obj = fileform.save(commit=False)
            file_obj.title = request.POST.get('title')
            file_obj.student = get_stu_session(request)
            file_obj.save()
            course = request.POST.get('course')
            create_time = request.POST.get('create_time')
            all_info = request.POST.get('all_info')

            return render(request, 'view_all_tasks_stu.html', all_info)

            # return redirect(
            #     reverse('view_all_tasks', kwargs={'course': course, 'create_time': create_time, 'all_info': all_info}))
        else:
            return render(request, 'detail_of_task.html', student_info)

@login_required
def view_all_tasks(request):
    en_name = get_stu_session(request)
    students = Student.objects.filter(en_name=en_name)
    for student in students:
        stu_class = student.class_name
        tasks = Assignment.objects.filter(class_name=stu_class)
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