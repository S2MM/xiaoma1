from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class SignUpForm(UserCreationForm):

    email = forms.EmailField(
        label = 'Email', 
        max_length = 254, 
        widget = forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
        }),
        help_text = '请输入合法的email地址'
    )
    username = forms.CharField(
        label = '用户名',
        max_length=32, 
        widget = forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
        }),     
        help_text='请输入用户名,这将是你在本站的名字'
    )
    password1 = forms.CharField(
        label = '密码', 
        widget = forms.PasswordInput(attrs={
            'class': 'form-control form-control-lg'
        }),
        help_text = '请输入密码', 
    )
    password2 = forms.CharField(
        label = '重复密码',
        widget = forms.PasswordInput(attrs={
            'class': 'form-control form-control-lg'
        }),
        help_text = '请再次输入密码'
    )

    class Meta:
        model = User
        fields = ('username', 'email')


