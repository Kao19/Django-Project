# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.utils import timezone

from django.contrib.auth.models import User

from django.urls import reverse

from django.shortcuts import redirect

from django.http import HttpResponseRedirect

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length = 100)
	content = models.TextField()
	date_posted = models.DateTimeField(default = timezone.now)
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	thumb = models.ImageField(default='SPACE.png',blank=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
			return HttpResponseRedirect.allowed_schemes.append('blog/urls/blog-home')
