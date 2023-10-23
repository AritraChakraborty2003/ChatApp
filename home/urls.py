from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [ 

    path('chat/<str:group_name>/',views.index,name="index"),
    path('',views.test,name="test")
  
]
