from django.urls import path

from .views import SignUpView, SignInView, signout

app_name = "accounts"

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('signout/', signout, name='signout'),
] 