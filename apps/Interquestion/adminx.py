#!/usr/bin/python3.6
# _*_ coding: utf-8 _*_
# @Author: sunshine
# @Time: 18-1-29 下午10:05
# @Software: PyCharm

import xadmin
from .models import InterviewCategory, InterviewQuestionBank, InterviewAssignment, \
    InterviewSubmission, InterviewCorrecting


class InterviewCategoryAdmin(object):
    list_display = ['category', 'created_time']
    search_fields = ['category']
    list_filter = ['category', 'created_time']


class InterviewQuestionBankAdmin(object):
    list_display = ['title', 'content', 'category', 'created_time',
                    'modified_time', 'creator', 'modifier']
    search_fields = ['title', 'content', 'category__category']
    list_filter = ['title', 'content', 'category', 'created_time',
                   'modified_time', 'creator', 'modifier']


class InterviewAssignmentAdmin(object):
    list_display = ['title', 'class_name', 'teacher', 'category',
                    'refer_complete_time', 'created_time']
    search_fields = ['title', 'times', 'class_name', 'teacher', 'category',
                     'refer_complete_time']
    list_filter = ['title', 'class_name', 'teacher', 'category',
                   'refer_complete_time', 'created_time']


class InterviewSubmissionAdmin(object):
    list_display = ['student', 'title', 'submit_answer', 'is_done',
                    'complete_time', 'is_delete', 'created_time']
    search_fields = ['student', 'title', 'submit_answer', 'is_done',
                     'complete_time', 'is_delete']
    list_filter = ['student', 'title', 'submit_answer', 'is_done',
                   'complete_time', 'is_delete', 'created_time']


class InterviewCorrectingAdmin(object):
    list_display = ['student', 'title', 'question_answer',
                    'is_right', 'created_time']
    search_fields = ['student', 'title', 'question_answer', 'is_right']
    list_filter = ['student', 'title', 'question_answer',
                   'is_right', 'created_time']


xadmin.site.register(InterviewCategory, InterviewCategoryAdmin)
xadmin.site.register(InterviewQuestionBank, InterviewQuestionBankAdmin)
xadmin.site.register(InterviewAssignment, InterviewAssignmentAdmin)
xadmin.site.register(InterviewSubmission, InterviewSubmissionAdmin)
xadmin.site.register(InterviewCorrecting, InterviewCorrectingAdmin)
