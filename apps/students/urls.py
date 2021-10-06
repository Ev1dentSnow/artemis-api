from django.urls import path, include

from apps.students import views
import apps.classes.views

urlpatterns = [
    path('', views.StudentsListView.as_view()),
    path('<int:student_user_id>', views.StudentInstanceView.as_view(), name='student instance view'),
    path('classes/', apps.classes.views.StudentClassesListView.as_view()),
    path('<int:student_user_id>/classes', apps.students.views.StudentInstanceClassesView.as_view()),
    path('<int:student_user_id>/marks/', include('apps.marks.urls')),
    path('<int:student_user_id>/dots/', include('apps.dots.urls')),
]