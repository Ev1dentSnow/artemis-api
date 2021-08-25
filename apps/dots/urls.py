from django.urls import path

from apps.dots import views

urlpatterns = [
    path('', views.DotsListView.as_view()),
]