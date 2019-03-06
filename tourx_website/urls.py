"""tourx_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from tourx import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('account/loggedin/', views.LoggedinView.as_view(), name='loggedin'),
    path('account/', include('django.contrib.auth.urls')),
    path('wait/', TemplateView.as_view(template_name='wait.html'), name='wait'),
    path('admin/', admin.site.urls, name='admin'),
    path('accounts/signup/', views.ProfileFormView.as_view(), name='signup'),


    # path('accounts/signup', TemplateView.as_view(template_name='signup.html'), name='sign'),
    # path('signin/', views.SigninView.as_view(), name='signin'),
    # path('login/', TemplateView.as_view(template_name='registration/loggedin.html'), name='login'),
]
