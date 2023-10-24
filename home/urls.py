from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [ 

    path('chat/<str:group_name>/',views.index,name="index"),
    path('chat/<str:group_name>/logout',views.logout,name="logout1"),
    path("main",views.test,name="main"),
    path('',views.test,name="test")
  
]
