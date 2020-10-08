from django.conf.urls import url,include
from django.urls import  path,re_path
from . import views
#from counterdb.views import  counter
urlpatterns = [
    path('', views.index),
    path('counter', views.counter),
    path('number_get', views.getnumber),
    path('number_free', views.freenumber),
    path('number_reg', views.regnumber)
]
