from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from .forms import LoginForm,SignupForm

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('articles:list')
    else:
        form = SignupForm
    return render(request,'accounts/sign_ju.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('articles:list')
    else:
        form = LoginForm
    return render(request,'accounts/sign.html',{'form':form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('articles:list')