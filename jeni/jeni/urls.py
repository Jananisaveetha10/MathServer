from django.contrib import admin 
from django.urls import path 
from jeniapp import views 
urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('powerofabulb/',views.powerofabulb,name="powerofabulb"),
    path('',views.powerofabulb,name="powerofabulbroot")
]