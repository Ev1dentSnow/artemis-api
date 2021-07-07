from django.urls import path

from apps.students import views

urlpatterns = [
    path('', views.StudentsList.as_view(), name='index'),
]