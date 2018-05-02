import xadmin

from .models import Teacher, ClassTeacher, TeacherUpload


class TeachersAdmin(object):
    list_display = ['en_name', 'real_name', 'gender', 'email', 'created_time']
    search_fields = ['en_name', 'real_name', 'gender', 'email']
    list_filter = ['en_name', 'real_name', 'gender', 'email', 'created_time']


class ClassTeacherAdmin(object):
    list_display = ['class_name', 'teacher', 'created_time']
    search_fields = ['class_name__name', 'teacher__en_name']
    list_filter = ['class_name', 'teacher', 'created_time']


class TeacherUploadAdmin(object):
    list_display = ['file', 'to_class', 'pub_time']
    search_fields = ['file', 'to_class', 'pub_time']
    list_filter = ['file', 'to_class', 'pub_time']


xadmin.site.register(Teacher, TeachersAdmin)
xadmin.site.register(ClassTeacher, ClassTeacherAdmin)
xadmin.site.register(TeacherUpload, TeacherUploadAdmin)
