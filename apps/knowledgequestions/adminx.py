import xadmin

from .models import Course, Module, KnowledgeBase, QuestionBank


class CourseAdmin(object):
    list_display = ['name', 'detail', 'difficulty_level', 'category', 'creator',
                    'modifier', 'created_time', 'modified_time']
    search_fields = ['name', 'detail', 'difficulty_level', 'category', 'creator', 'modifier']
    list_filter = ['name', 'detail', 'difficulty_level', 'category', 'creator',
                   'modifier', 'created_time', 'modified_time']


class ModuleAdmin(object):
    list_display = ['course', 'name', 'creator', 'modifier', 'created_time', 'modified_time']
    search_fields = ['course__name', 'name']
    list_filter = ['course', 'name', 'creator', 'modifier', 'created_time', 'modified_time']


class KnowledgeBaseAdmin(object):
    list_display = ['module', 'name', 'knowledge_point', 'creator',
                    'modifier', 'created_time', 'modified_time']
    search_fields = ['module__name', 'name', 'knowledge_point']
    list_filter = ['module', 'name', 'knowledge_point', 'creator',
                   'modifier', 'created_time', 'modified_time']


class QuestionBankAdmin(object):
    list_display = ['title', 'content', 'difficulty_level', 'knowledgebase', 'creator',
                    'modifier', 'created_time', 'modified_time']
    search_fields = ['title', 'content', 'difficulty_level', 'knowledgebase__name']
    list_filter = ['title', 'content', 'difficulty_level', 'knowledgebase', 'creator',
                   'modifier', 'created_time', 'modified_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Module, ModuleAdmin)
xadmin.site.register(KnowledgeBase, KnowledgeBaseAdmin)
xadmin.site.register(QuestionBank, QuestionBankAdmin)
