"""EducationPlatform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
import xadmin, students, homework, teachers, Interquestion.views
from students.views import StuRegisterView, StuLoginView, StuRegisterInfoView, view_course_ware
from teachers.views import TchRegisterView, TchLoginView, TchRegisterInfoView, UploadView
from homework.views import PublishView, SubmitView, ViewTheDegreeOfCompletionView
from Interquestion.views import *
from django.views.static import serve
from EducationPlatform.settings import MEDIA_ROOT

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),

    url(r'^homepage_stu/$', students.views.homepage_stu, name='homepage_stu'),
    url(r'^register_stu/$', StuRegisterView.as_view(), name="register_stu"),
    url(r'^register_info_stu/$', StuRegisterView.as_view(), name="register_info_stu"),
    url(r'^submit_register_info_stu/$', StuRegisterInfoView.as_view(), name="submit_register_info_stu"),
    url(r'^login_stu/$', StuLoginView.as_view(), name='login_stu'),
    url(r'^submit_login_info_stu/$', StuLoginView.as_view(), name='submit_login_info_stu'),
    url(r'^view_all_tasks/$', homework.views.view_all_tasks, name='view_all_tasks'),
    url(r'^detail_of_task/$', SubmitView.as_view(), name='detail_of_task'),
    url(r'^submit_answer/$', SubmitView.as_view(), name='submit_answer'),
    url(r'^logout_stu/$', students.views.logout_stu, name='logout_stu'),
    url(r'^search_interview_questions/$', QuestionDetailView.as_view(), name='search_interview_questions'),
    url(r'^search_question_detail/$', SubmitAnswerView.as_view(), name='search_question_detail'),
    url(r'^submit_interviewquestions_answer/$', SubmitAnswerView.as_view(), name='submit_interviewquestions_answer'),
    url(r'^cuotiji/$', SearchWrongQuestions.as_view(), name='cuotiji'),
    url(r'^cuotiji_detail/$', SearchWrongQuestions.as_view(), name='cuotiji_detail'),

    url(r'^homepage_tch/$', teachers.views.homepage_tch, name='homepage_tch'),
    url(r'^register_tch/$', TchRegisterView.as_view(), name="register_tch"),
    url(r'^register_info_tch/$', TchRegisterInfoView.as_view(), name="register_info_tch"),
    url(r'^submit_register_info_tch/$', TchRegisterInfoView.as_view(), name="submit_register_info_tch"),
    url(r'^login_tch/$', TchLoginView.as_view(), name='login_tch'),
    url(r'^submit_login_info_tch/$', TchLoginView.as_view(), name='submit_login_info_tch'),
    url(r'^publish_tasks/$', PublishView.as_view(), name='publish_tasks'),
    url(r'^submit_course_info/$', PublishView.as_view(), name='submit_course_info'),
    url(r'^submit_module_info/$', homework.views.submit_module_info, name='submit_module_info'),
    url(r'^submit_knowledgebase_info/$', homework.views.submit_knowledgebase_info, name='submit_knowledgebase_info'),
    url(r'^submit_tasks_info/$', homework.views.submit_tasks_info, name='submit_tasks_info'),
    url(r'^view_the_degree_of_completion_tch/$', ViewTheDegreeOfCompletionView.as_view(),
        name='view_the_degree_of_completion_tch'),
    url(r'^view_detail_of_completion_tch/$', ViewTheDegreeOfCompletionView.as_view(),
        name='view_detail_of_completion_tch'),
    url(r'^logout_tch/$', teachers.views.logout_tch, name='logout_tch'),
    url(r'^upload/$', UploadView.as_view(), name='upload'),
    url(r'^publish_interviewquestions/$', PublishInterQuesView.as_view(), name='publish_interviewquestions'),
    url(r'^publish_interview_tasks/$', PublishInterQuesView.as_view(), name='publish_interview_tasks'),
    url(r'^get_all_questions/$', Interquestion.views.get_all_questions, name='get_all_questions'),
    url(r'^inspact_answer/$', LookOverView.as_view(), name='inspact_answer'),
    url(r'^modify_answer/$', ModifyView.as_view(), name='modify_answer'),
    url(r'^submit_modify_content/$', ModifyView.as_view(), name='submit_modify_content'),
    url(r'^view_course_ware/$', students.views.view_course_ware, name='view_course_ware'),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    url(r'^get_stu_list/$', StuListView.as_view(), name='get_stu_list'),
    url(r'^submit_class_info/$', Interquestion.views.submit_class_info, name='submit_class_info'),
    url(r'^get_stu_list/submit_stu_info/$', LookOverView.as_view(), name='get_stu_list/submit_stu_info'),

]
