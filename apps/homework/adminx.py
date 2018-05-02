import xadmin
from .models import Assignment, Submission


class AssignmentAdmin(object):
    list_display = ['title', 'class_name', 'teacher', 'course', 'first_module',
                    'second_module', 'is_bonus', 'refer_complete_time', 'created_time']
    search_fields = ['title', 'class_name', 'teacher', 'course', 'first_module',
                     'second_module', 'is_bonus', 'refer_complete_time']
    list_filter = ['title', 'class_name', 'teacher', 'course', 'first_module',
                   'second_module', 'is_bonus', 'refer_complete_time', 'created_time']


class SubmissionAdmin(object):
    list_display = ['student', 'title', 'submit_answer', 'is_done', 'created_time']
    search_fields = ['student', 'title', 'submit_answer', 'is_done']
    list_filter = ['student', 'title', 'submit_answer', 'is_done', 'created_time']


xadmin.site.register(Assignment, AssignmentAdmin)
xadmin.site.register(Submission, SubmissionAdmin)
