from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout


from .forms import SignUpForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('/')