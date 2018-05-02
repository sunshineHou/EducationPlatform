import xadmin

from .models import Class


class ClassAdmin(object):
    list_display = ['name', 'major', 'administrator', 'created_time', 'modified_time']
    search_fields = ['name', 'major', 'administrator']
    list_filter = ['name', 'major', 'administrator', 'created_time', 'modified_time']


xadmin.site.register(Class, ClassAdmin)
