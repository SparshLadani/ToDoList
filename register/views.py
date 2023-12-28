from django.contrib.auth import logout
from django.shortcuts import render, redirect
from .forms import SignUp

# Create your views here.

def register(response):
    if response.method == "POST":
        form = SignUp(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = SignUp()
    return render(response, 'register/Register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/')# Redirect to a success page.