from django.urls import path

from apps.announcements import views

urlpatterns = [
    path('', views.AnnouncementsListView.as_view()),
    path('<int:announcement_id>', views.AnnouncementInstanceView.as_view()),
]