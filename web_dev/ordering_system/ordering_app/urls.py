from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('products/', views.ProductView.as_view()),
    path('orders/', views.OrderView.as_view()),
    path('orders/<int:order_id>/', views.OrderDetailView.as_view()),
]
