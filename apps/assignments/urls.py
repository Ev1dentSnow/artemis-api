from django.urls import path

import apps.assignments.views

urlpatterns = [
    path('', apps.assignments.views.AssignmentsListView.as_view()),
]