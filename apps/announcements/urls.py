from django.urls import path

from apps.announcements import views

urlpatterns = [
    path('', views.AnnouncementsList.as_view()),
]