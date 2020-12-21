from django.conf.urls import url
from . import views
from .views import PostListView, PostDetailView, PostCreateView

urlpatterns = [
    url(r'^$', PostListView.as_view() , name='blog-home'),
    url(r'^post/<pk>/', PostDetailView.as_view() , name='post-detail'), #doesn't work
    url(r'^post/new/', PostCreateView.as_view() , name='post-create'),
    url(r'^about/', views.about , name='blog-about'),

]