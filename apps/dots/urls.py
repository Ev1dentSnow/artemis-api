from django.urls import path
import apps.students.views

urlpatterns = [
    path('', apps.students.views.StudentInstanceDotsView.as_view()),
    path('<int:dot_id>', apps.students.views.StudentInstanceDotsInstanceView.as_view())
]