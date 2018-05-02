#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author : dengguo
# @Time : 18-1-3 下午19:31
# @Software: PyCharm

from django.test import TestCase
from django.core.urlresolvers import resolve
import teachers
from teachers import views

# Create your tests here.

class HomepageTest(TestCase):
    def test_url_homepage_tch_resolves_to_homepage_tch_view(self):
        found = resolve('/homepage_tch/')
        self.assertEqual(found.func, teachers.views.homepage_tch)

class TchRegisterTest(TestCase):
    def test_url_register_tch_resolves_to_register_tch_view(self):
        found = resolve('/register_tch/')
        self.assertEqual(found.func, teachers.views.TchRegisterView)