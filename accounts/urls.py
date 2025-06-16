from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name= 'register'),
    path('login/', views.UserLoginView.as_view(), name= 'login'),
    path('logout/', views.UserLogoutView.as_view(), name= 'logout'),
    path('profile/', views.ProfileView.as_view(), name= 'profile'),
    path('deposit/', views.DepositView.as_view(), name= 'deposit'),
    path('return/<int:pk>', views.ReturnBookView.as_view(), name= 'return'),
]