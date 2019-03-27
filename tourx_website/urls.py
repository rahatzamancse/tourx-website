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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView, DetailView, ListView

from tourx import views
from tourx.models import Counter

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('account/loggedin/', views.LoggedinView.as_view(), name='loggedin'),
    path('account/', include('django.contrib.auth.urls')),
    path('wait/', TemplateView.as_view(template_name='wait.html'), name='wait'),
    path('admin/', admin.site.urls, name='admin'),
    path('accounts/signup/', views.ProfileFormView.as_view(), name='signup'),

    path('tour/<val>/', views.tour, name='tour'),

    path('hotel/<val>/', views.hotel, name='hotel'),
    path('counters/', ListView.as_view(template_name='counters.html', model=Counter), name='counters')


    # path('accounts/signup', TemplateView.as_view(template_name='signup.html'), name='sign'),
    # path('signin/', views.SigninView.as_view(), name='signin'),
    # path('login/', TemplateView.as_view(template_name='registration/loggedin.html'), name='login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
