from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('teams/', views.CreateTeamView.as_view()),
    path('teams/<int:team_id>/', views.TeamView.as_view()),
    path('teams/<int:team_id>/edit/', views.EditTeamView.as_view()),
    path('teams/<int:team_id>/delete/', views.DeleteTeamView.as_view()),
    path('teams/<int:team_id>/players/', views.AddPlayerView.as_view()),
    path('teams/<int:team_id>/<int:player_id>/', views.DeletePlayerView.as_view()),
]
