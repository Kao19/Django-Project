# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

from PIL import Image

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default_profile.png',upload_to='profile_pics')

	def __str__(self):
		return '{self.user.username} Profile' 

	def save(self, *args, **kwargs):
			super(Profile,self).save(*args, **kwargs)

			img = Image.open(self.image.path)	

			if img.height > 300 or img.width > 300:
			   output_size = (300, 300)
			   img.thumbnail(output_size)
			   img.save(self.image.path) 

#i need to pip install pillow but it doesn't work so i won't add profiles ==== fixed


    

