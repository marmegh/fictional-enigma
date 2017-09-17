# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def display(request):
    return HttpResponse('placeholder to display all the surveys created')
def new(request):
    return HttpResponse('placeholder to create new surveys')