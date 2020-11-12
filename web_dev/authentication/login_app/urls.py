from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('register/', views.RegistrationView.as_view()),
    path('login/', views.LoginView.as_view()),
    # path('home/', views.HomeView.as_view()),
    path('home/', views.home_page),
    path('logout/', views.LogoutView.as_view()),
]
