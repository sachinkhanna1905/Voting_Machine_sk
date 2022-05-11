
from django.contrib import admin
from django.urls import path
from Poll_App import views

urlpatterns = [
    
    # http://127.0.0.1:8000
    path('home',views.home,name="Home"),
    
    path('result/<poll_id>',views.result,name="Result"),
    path('vote/<poll_id>',views.vote,name="Vote"),
    
]
