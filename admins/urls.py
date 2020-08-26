from . import views

from django.urls import path

urlpatterns = [
    path('', views.SignInView.as_view(), name='login-page'),
    path('logout/', views.SignOutView.as_view(), name='logout-page')
]