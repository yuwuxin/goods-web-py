#!/usr/bin/env python
# _*_coding:utf-8_*_
# Author:li hang

# from django.http import HttpResponse
#
#
# def hello(request):
#     return HttpResponse("Hello world ! ")

from django.shortcuts import render

def index(request):
    context = {}
    context['title'] = 'hello world'
    return render(request, 'index.html', context)