from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('register/', views.RegistrationView.as_view()),
]
