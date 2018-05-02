#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author : dengguo
# @Time : 18-2-1 上午11:01
# @File : ysf.py
# @Software: PyCharm

def ysf(n,k,m):
    list1 = [x for x in range(1,n+1)]
    t = k-1
    for i in range(n-1):
        t = (t+m-1)%len(list1)
        print("Out:",list1.pop(t))
    print("留下的编号为： "+str(list1[0]))
ysf(6,1,3)