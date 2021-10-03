from django.urls import path

from apps.teachers import views

urlpatterns = [
    path('', views.TeachersListView.as_view()),
    path('<int:teacher_user_id>', views.TeacherInstanceView.as_view()),
    path('<int:teacher_user_id>/classes', views.TeacherClassesView.as_view()),
]


