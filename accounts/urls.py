from rest_auth.registration.views import VerifyEmailView

from django.conf.urls import url

from . import views


urlpatterns = [
    url('register/', views.UserRegisterView.as_view(), name='register'),
    url('account-confirm-email/(?P<key>[-:\w]+)/$', VerifyEmailView.as_view(),
        name='account_confirm_email'),
]
