from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('teams/', views.CreateTeamView.as_view()),
    path('teams/<int:team_id>/', views.TeamView.as_view()),
]
