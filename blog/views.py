# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from .models import Post

from django.views.generic import ListView, DetailView, CreateView


# Create your views here.
def home(request):
	context =  {
	   'posts' : Post.objects.all()
	}
	return render(request, 'blog/home.html', context)


class PostListView(ListView):
  model = Post
  template_name = 'blog/home.html'
  context_object_name = 'posts'
  ordering = ['-date_posted'] #to make the newist post appear at the top 

class PostDetailView(DetailView):
  model = Post

class PostCreateView(CreateView):
  model = Post
  fields = ['title' , 'content' , 'thumb']

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super(PostCreateView, self).form_valid(form)
    

def about(request):
	return render(request, 'blog/about.html' , {'title': 'About'})






