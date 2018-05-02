#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author : dengguo
# @Time : 18-1-3 下午3:26
# @Software: PyCharm
from django.test import TestCase
from django.core.urlresolvers import resolve
from students import views
from students.views import homepage_stu, StuRegisterView
from django.http import HttpRequest, HttpResponse
from django.template.loader import render_to_string
# Create your tests here.

class HomepageTest(TestCase):

    def test_url_homepage_stu_resolves_to_homepage_stu_view(self):
        found = resolve('/homepage_stu/')
        self.assertEqual(found.func, views.homepage_stu)

    def test_url_homepage_stu_returns_correct_html(self):
        request = HttpRequest()
        response = homepage_stu(request)
        except_html = render_to_string('home_page_stu.html')
        self.assertEqual(response.content.decode(), except_html)

class RegisterTest(TestCase):

    # def test_url_register_stu_resolves_to_register_stu_view(self):
    #     found = resolve('/register_stu/')
    #     self.assertEqual(found.func, StuRegisterView)

    def test_url_register_stu_returns_correct_html(self):
        pass
    #
    # def test_url_register_info_stu_resolves_to_register_info_stu_view(self):
    #     found = resolve('/register_info_stu/')
    #     self.assertEqual(found.func, StuRegisterView)

class LoginTest(TestCase):
    pass

