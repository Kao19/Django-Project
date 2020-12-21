from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created , **kwargs):
	if created:
		Profile.objects.create(user=instance)
 
 #we have a sender and a signal of post_save, when a user is saved then send this signal (post_save) and that
#signal is going to be recieved by the reciever . the reciever is the create_profile function
#this function take the instance of the user. so if the user was created we need to creat a profile object
#where the user is egual to the instance of the user that was created

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
	instance.profile.save()

	#to save our profile
