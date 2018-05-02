import xadmin

from .models import Student


class StudentsAdmin(object):
    list_display = ['en_name', 'real_name', 'gender', 'mobile', 'class_name', 'created_time']
    search_fields = ['en_name', 'real_name', 'gender', 'mobile', 'class_name__name']
    list_filter = ['real_name', 'en_name', 'gender', 'mobile', 'class_name', 'created_time']


xadmin.site.register(Student, StudentsAdmin)
