from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index),
    path('', views.CreateUserView.as_view()),
    path('read/', views.GetUsersView.as_view()),
    path('countries/', views.countries),
    path('states/', views.states),
    path('login/', views.login_view.as_view()),
    path('r/<str:page_name>/', views.reddit_view.as_view()),
]
