from django.conf.urls import url
from . import views
from .views import *

urlpatterns = [url(r'^get/$', views.getdata, name = 'getdata'),
			   url(r'^gen/$', views.gendata ,name = 'gendata')]