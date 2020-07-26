"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
import myapp.views
import pos.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('table1/', myapp.views.home, name='home'),
    path('table1/m1/', pos.views.m1, name='home'),
    path('table1/m2/', pos.views.m2, name='home'),
    path('table1/m3/', pos.views.m3, name='home'),
    path('table1/m4/', pos.views.m4, name='home'),
    path('table1/m5/', pos.views.m5, name='home'),
    path('pos/', pos.views.home, name='pos'),
    path('pos/new/', pos.views.new, name='new'),
    path('pos/detail/<int:biog_id>/', pos.views.detail, name='detail'),
    path('pos/create/', pos.views.create, name='create'),
    path('pos/postcreate/', pos.views.postcreate, name='postcreate'),
    path('pos/update/<int:blog_id>/', pos.views.update, name='update'),
    path('pos/delete/<int:blog_id>/', pos.views.delete, name='delete'),
    path('pos/start/', pos.views.start, name='start'),
    path('pos/download/', pos.views.download, name='download'),
]
