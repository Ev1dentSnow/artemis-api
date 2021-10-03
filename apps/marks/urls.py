from django.urls import path, include

import apps.students.views

urlpatterns = [
    path('', apps.students.views.StudentInstanceMarksListView.as_view()),
    path('<int:mark_id>', apps.students.views.StudentInstanceMarksInstanceView.as_view()),
]
