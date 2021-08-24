from django.urls import path
from apps.classes import views

urlpatterns = [
    path('', views.ClassesListView.as_view()),
    #path('classes', views.StudentClassesListView.as_view()),
]


