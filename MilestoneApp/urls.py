from django.urls import path
from . import views


urlpatterns = [
    path('projects/', views.projects, name='projects'),
    path('students/', views.students, name='students'),
    path('groupmembers/', views.group_members, name='group_members'),
]
