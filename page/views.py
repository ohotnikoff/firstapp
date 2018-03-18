# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http.response import HttpResponse, Http404

# Create your views here.
def home(request):
    return render(request, 'page/home.html')

def about(request):
    return render(request, 'page/about.html')