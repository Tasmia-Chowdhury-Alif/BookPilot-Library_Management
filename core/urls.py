from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name= 'home'),
    path('category/<slug:category_slug>/', views.HomeView.as_view(), name= 'category-wise'),
]