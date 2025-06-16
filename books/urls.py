from django.urls import path, include
from . import views

urlpatterns = [
    path('book/<int:pk>/', views.BookDetailsView.as_view(), name= 'details'),
    path('borrow/<int:pk>/', views.BorrowView.as_view(), name= 'borrow'),
]