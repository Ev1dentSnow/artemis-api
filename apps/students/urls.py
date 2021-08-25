from django.urls import path, include

from apps.students import views
import apps.classes.views

urlpatterns = [
    path('', views.StudentsListView.as_view()),
    path('<int:student_user_id>', views.StudentInstanceView.as_view()),
    path('classes/', apps.classes.views.StudentClassesListView.as_view()),
    #path('classes/', include('apps.classes.urls')),
    path('<int:student_user_id>/classes', apps.students.views.StudentInstanceClassesView.as_view()),
    path('<int:student_user_id>/marks', apps.students.views.StudentInstanceMarksView.as_view()),
]