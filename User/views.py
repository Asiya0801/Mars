from django.shortcuts import render
from .models import *
from .forms import *

def dashboard(request):
    products = Product.objects.all()
    return render(request, 'dashboard.html', {'products':products})

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'login.html')
        else:
            return render(request, "Error.html")
    else:
        form = UserForm()
    return render(request, 'register.html', {'form':form})   

def Login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, "dashboard.html")
        else:
            return render(request, "Error.html")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form':form})

def addproduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'dashboard.html')
        else:
            return render(request, 'error.html')
    else:
        form = ProductForm()
        return render(request, 'add.html', {'form':form})