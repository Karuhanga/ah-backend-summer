from django.urls import path

from .views import (
    LoginAPIView, RegistrationAPIView, UserRetrieveUpdateAPIView,
    TwitterAuthAPIView, GoogleAuthAPIView, FacebookAuthAPIView,
    AccountActivateAPIView,

    PasswordResetRequestAPIView, PasswordResetAPIView
)
app_name = "authentication"
urlpatterns = [
    path('user', UserRetrieveUpdateAPIView.as_view(),
         name='retrieve-update'),
    path('users', RegistrationAPIView.as_view(),
         name='register'),
    path('users/login', LoginAPIView.as_view(),
         name='login'),
    path('users/login/twitter', TwitterAuthAPIView.as_view(),
         name='twitter-auth'),
    path('users/login/google', GoogleAuthAPIView.as_view(),
         name='google-auth'),
    path('users/login/facebook', FacebookAuthAPIView.as_view(),
         name='facebook-auth'),
    path('users/<token>', AccountActivateAPIView.as_view(),
         name='activate'),
    path(
        'user/request-password-reset', PasswordResetRequestAPIView.as_view(),
        name='request-password-reset'
    ),
    path(
        'user/reset-password/<token>', PasswordResetAPIView.as_view(),
        name='reset-password'
    ),
]
