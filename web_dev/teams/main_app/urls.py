from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('team/<int:team_id>/', views.TeamView.as_view()),
]
