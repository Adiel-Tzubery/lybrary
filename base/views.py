from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User







def home(request):
    return render(request, 'base/home.html')



def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponse('user is logged in (github branch check)')

    else:
        form = LoginUserForm()
        return render(request, 'base/login_page.html', {'form': form})


def logoutUser(request):
    pass