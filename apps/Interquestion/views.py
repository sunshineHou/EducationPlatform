#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author : dengguo

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse
from django.views.generic import View
from .models import InterviewQuestionBank, InterviewAssignment, InterviewSubmission, InterviewCategory, \
    InterviewCorrecting
import json
from homework.views import *


# Create your views here.

@login_required
def get_all_questions(request):
    if request.method == "GET":
        course_info = request.GET.get('q')
        course = InterviewCategory.objects.filter(category=course_info)
        questions = InterviewQuestionBank.objects.filter(category=course)
        question_dict = {}
        for question in questions:
            question_name = question.title
            question_dict['%s' % question_name] = question_name
        return HttpResponse(json.dumps(question_dict), content_type="application/json")


class PublishInterQuesView(View):
    def get(self, request):
        classes = Class.objects.all()
        courses = InterviewCategory.objects.all()
        courses_info = {
            'classes': classes,
            'courses': courses,
        }
        return render(request, 'publish_Interviewquestions.html', courses_info)

    def post(self, request):
        question_title = request.POST.getlist('is_release')
        class_name = request.POST.get('class_name')
        course = request.POST.get('course')

        interviewAssignment = InterviewAssignment()

        interviewAssignment.title = question_title
        interviewAssignment.category = course
        interviewAssignment.teacher = get_tch_session(request)
        interviewAssignment.class_name = class_name

        interviewAssignment.save()

        return self.get(request)


class QuestionDetailView(View):
    def get(self, request):
        questions = InterviewAssignment.objects.all()
        result_list = []
        for question in questions:
            question_list = question.title
            target_list = question_list.replace("['", '').replace("']", '').split("', '")
            results = result_list.append(target_list)
        all_info = {
            'questions': questions,
            'en_name': get_stu_session(request),
            'results': results,
        }
        return render(request, 'search_all_questions.html', all_info)


class SubmitAnswerView(View):
    def get(self, request):
        create_time = request.GET.get('create_time')
        course = request.GET.get('course')
        all_info = request.GET.get('all_info')

        interviewAssignments = InterviewAssignment.objects.filter(category=course)
        for interviewAssignment in interviewAssignments:
            title_list = interviewAssignment.title
            title_list = title_list.replace("['", '').replace("']", '').split("', '")
            print(title_list)
            print(type(title_list))
            question_list = []
            for title in list(title_list):
                interviewQuestionBanks = InterviewQuestionBank.objects.filter(title=title)
                for interviewQuestionBank in interviewQuestionBanks:
                    question_list.append(interviewQuestionBank)
            info = {
                'question_list': question_list,
                'en_name': get_stu_session(request),
                'all_info': all_info,
                'create_time': create_time,
                'course': course
            }
            return render(request, 'search_question_detail.html', info)

    def post(self, request):
        question_title = request.POST.getlist('title')
        question_answer = request.POST.getlist('answer')
        student = get_stu_session(request)
        print(question_title, question_answer, student)

        interviewSubmission = InterviewSubmission()
        interviewSubmission.title = question_title
        interviewSubmission.student = student

        interviewSubmission.submit_answer = question_answer

        interviewSubmission.save()
        return QuestionDetailView.get(self, request)


def submit_class_info(request):
    if request.method == 'GET':
        class_name = request.GET.get('q')
        class_object = Class.objects.get(name=class_name)
        students = class_object.get_all_students()
        student_dict = {}
        for student in students:
            student_name = student.en_name
            student_dict['%s' % student_name] = student_name
        return HttpResponse(json.dumps(student_dict), content_type="application/json")


class StuListView(View):
    def get(self, request):
        classes = Class.objects.all()
        class_info = {
            'en_name': get_tch_session(request),
            'classes': classes,
        }
        return render(request, 'stu_list.html', class_info)

    def post(self, request):
        pass


class LookOverView(View):
    def get(self, request):
        questions = InterviewAssignment.objects.all()
        result_list = []
        for question in questions:
            question_list = question.title
            target_list = question_list.replace("['", '').replace("']", '').split("', '")
            results = result_list.append(target_list)
        all_info = {
            'questions': questions,
            'en_name': get_tch_session(request),
            'results': results,
        }
        return render(request, 'zuoyeqingdan.html', all_info)


class ModifyView(View):
    def get(self, request):
        create_time = request.GET.get('create_time')
        course = request.GET.get('course')
        all_info = request.GET.get('all_info')

        interviewAssignments = InterviewAssignment.objects.filter(category=course)
        for interviewAssignment in interviewAssignments:
            interviewSubmissions = InterviewSubmission.objects.filter(id=interviewAssignment.id)
            for interviewSubmission in interviewSubmissions:
                answer_list = interviewSubmission.submit_answer
                answer_list = answer_list.replace("['", '').replace("']", '').split("', '")
                print(answer_list)
            for interviewAssignment in interviewAssignments:
                title_list = interviewAssignment.title
                title_list = title_list.replace("['", '').replace("']", '').split("', '")
                question_list = []
                for title in list(title_list):
                    interviewQuestionBanks = InterviewQuestionBank.objects.filter(title=title)
                    for interviewQuestionBank in interviewQuestionBanks:
                        question_list.append(interviewQuestionBank)
                        print('%%%%%%%%%%', question_list)
                info = {
                    # 'answer_list': answer_list,
                    'question_list': question_list,
                    'en_name': get_tch_session(request),
                    'all_info': all_info,
                    'create_time': create_time,
                    'course': course
                }
                return render(request, 'cheack_answer.html', info)

    def post(self, request):
        question_answer = request.POST.getlist('answer')
        title = request.POST.getlist('title')
        is_right = request.POST.getlist('is_right')
        student = get_stu_session(request)

        interviewCorrecting = InterviewCorrecting()
        interviewCorrecting.student = student
        interviewCorrecting.is_right = is_right
        interviewCorrecting.title = title
        interviewCorrecting.question_answer = question_answer

        interviewCorrecting.save()

        return StuListView.get(self, request)


class SearchWrongQuestions(View):
    def get(self, request):
        questions = InterviewAssignment.objects.all()
        result_list = []
        for question in questions:
            question_list = question.title
            target_list = question_list.replace("['", '').replace("']", '').split("', '")
            results = result_list.append(target_list)
        all_info = {
            'questions': questions,
            'en_name': get_stu_session(request),
            'results': results,
        }

        return render(request, 'cuotiji.html', all_info)

    def post(self, request):
        if request.method == 'POST':
            create_time = request.GET.get('create_time')
            course = request.GET.get('course')
            all_info = request.GET.get('all_info')

            interviewCorrectings = InterviewCorrecting.objects.filter(is_right=0)
            info = {
                'interviewCorrectings': interviewCorrectings,
            }
            return render(request, 'cuoti_detail.html', info, all_info)
        else:
            return HttpResponse('method is not allowed')


class SearchWrongQuestionsDetail(View):
    def get(self, request):
        pass

    def post(self, request):
        pass