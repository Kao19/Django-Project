"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from users import views as user_views


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('blog.urls') ),
    url(r'^register/',user_views.register,name='register'),
    url(r'^profile/',user_views.profile,name='profile'),
    url(r'^login/',auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    url(r'^logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    url(r'^password-reset/',auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    url(r'^password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    url(r'^password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    url(r'^password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
