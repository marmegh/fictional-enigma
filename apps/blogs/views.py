# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return HttpResponse("placeholder to later display all the list of blogs")
def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")
def create(request):
    return redirect('/blogs')
def show(request):
    return HttpResponse('placeholder to display blog {{number}}')
def edit(request):
    return HttpResponse('placeholder to edit blog {{number}}')
def destroy(request):
    return redirect('/blogs')