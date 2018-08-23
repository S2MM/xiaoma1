from django.urls import path
from django.contrib.auth import views as auth_views

from .views import signup,signout

app_name = "accounts"

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('signin/', auth_views.LoginView.as_view(template_name="accounts/signin.html"), name='signin'),
    path('signout/', signout, name='signout'),
] 