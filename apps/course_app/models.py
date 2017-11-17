# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.db import models

class CourseManager(models.Manager):
	def basic_validator(self, postData):
		errors = {}
		if len(postData['name']) < 6:
			errors['name'] = "Course name should be more than 5 characters"
		elif any(char.isdigit() for char in postData['name']) == True:
			errors['name'] = "Course name shouldn't contain numbers"
		if len(postData['desc']) < 16:
			errors['desc'] = "Description should be more than 15 characters"
		elif any(char.isdigit() for char in postData['desc']) == True:
			errors['desc'] = "Description shouldn't contain numbers"
		return errors

class Course(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CourseManager()
