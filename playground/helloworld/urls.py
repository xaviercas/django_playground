# -*- coding: utf-8 -*-
# @Author: xavier
# @Date:   2018-03-05 21:37:48
# @Last Modified by:   xavier
# @Last Modified time: 2018-03-05 21:47:51

from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
]
