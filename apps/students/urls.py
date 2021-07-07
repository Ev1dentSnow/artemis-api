from django.urls import path

from apps.students import views

urlpatterns = [
    path('', views.StudentsListView.as_view()),
    path('<int:student_user_id>', views.StudentInstanceView.as_view()),
]