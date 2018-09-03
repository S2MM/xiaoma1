from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

ERROR_MESSAGE = "用户名 或 密码 - 不正确"
ERROR_MEESAGE_INACTIVE = "此用户未激活"

class SignUpForm(UserCreationForm):

    email = forms.EmailField(
        label = 'Email', 
        max_length = 254, 
        help_text = '请输入合法的email地址'
    )
    username = forms.CharField(
        label = '用户名',
        max_length=32,   
        help_text='请输入用户名,这将是你在本站的名字'
    )
    password1 = forms.CharField(
        label = '密码', 
        help_text = '请输入密码', 
    )
    password2 = forms.CharField(
        label = '重复密码',
        help_text = '请再次输入密码'
    )

    class Meta:
        model = User
        fields = ('username', 'email')

class SignInForm(AuthenticationForm):

    username = forms.EmailField(
        label = '电子邮箱', 
        max_length = 254, 
    )

    message_incorrect_password = ERROR_MESSAGE
    message_inactive = ERROR_MEESAGE_INACTIVE

    '''
    def clean(self):
        email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        print("email 是： ", email)
        print('password 是：', password)

        if email is not None and password:
            self.user_cache = authenticate(email=email, password=password)
            if (self.user_cache is None):
                raise forms.ValidationError(self.message_incorrect_password)
            if not self.user_cache.is_active:
                raise forms.ValidationError(self.message_inactive)

        return self.cleaned_data
    '''