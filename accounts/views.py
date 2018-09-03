from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, authenticate, logout

from .forms import SignUpForm, SignInForm 

# Create your views here.
class SignUpView(View):
    form_class = SignUpForm
    template_name = 'accounts/signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, { 'form': form })

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        return render(request, self.template_name, {'form': form})


class SignInView(View):
    form_class = SignInForm
    template_name = 'accounts/signin.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, { 'form': form })

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=email, password=password)
            login(request, user)
            return redirect('/')
        else:
            print(form.error_messages)
        return render(request, self.template_name, { 'form': form })
            


def signout(request):
    logout(request)
    return redirect('/')