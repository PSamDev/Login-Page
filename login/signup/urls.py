from django.urls import path 
from . import views
from . views import SignUpView
from django.contrib.auth import views as auth_views

app_name = "site"

urlpatterns = [
    path("", views.home, name="home"),
    path("welcome/", views.welcome, name="welcome"),
    path("profile/", views.profile, name="profile"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]
