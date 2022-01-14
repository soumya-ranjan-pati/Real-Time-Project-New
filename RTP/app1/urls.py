from django.contrib import admin
from django.urls import path
from app1 import views
urlpatterns = [
    path('',views.showindex,name='main'),
    path('registration/',views.registration,name='registration'),
    path('user_registration/',views.registration,name='user_registration'),
]

