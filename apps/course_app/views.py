# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import *

def index(request):
	if request.session.get('id') is None:
		request.session['id'] = 0
	return render(request, 'course_app/index.html', {"courses": Course.objects.all()})

def create(request):
	errors = Course.objects.basic_validator(request.POST)
	if len(errors):
		for key, value in errors.iteritems():
			messages.error(request, value)
		return redirect('/')
	else:
		Course.objects.create(name=request.POST['name'], desc=request.POST['desc'])
		return redirect('/')

def confirm(request, number):
	request.session['id'] = int(number)
	return render(request, 'course_app/confirmDestroy.html', {"course":Course.objects.get(id=number)})

def destroy(request):
	Course.objects.get(id=request.session['id']).delete()
	return redirect('/')


	

