from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def login_user(request):
    if request.method == 'POST':
        pass
        username = request.POST['username'] #Username: admin
        password = request.POST['password'] #Password: EliteEats
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, "Incorrect Username or Password. Try Again.")
            return redirect('login')
        
    else:
        return render(request, 'authenticate/login.html', {})