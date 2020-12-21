# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Profile

# Register your models here.

admin.site.register(Profile)

#this is importent to be able to see the users profile on the admin page of our website