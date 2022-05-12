from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.
from homeservice_app.forms import LoginRegister, WorkerRegister, CustomerRegister


def home(request):
    return render(request, 'home.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('admin_home')
            elif user.is_worker:
                return redirect('worker_home')
            elif user.is_customer:
                return redirect('customer_home')

        else:
            messages.info(request, 'Invalid Credentials')
    return render(request, 'login.html')


def worker_register(request):
    user_form = LoginRegister()
    worker_form = WorkerRegister()
    if request.method == 'POST':
        user_form = LoginRegister(request.POST)
        worker_form = WorkerRegister(request.POST, request.FILES)
        if user_form.is_valid() and worker_form.is_valid():
            user = user_form.save(commit=False)
            user.is_worker = True
            user.save()
            worker = worker_form.save(commit=False)
            worker.user = user
            worker.save()
            messages.info(request, 'Registered Successfully')
            return redirect('login')
    return render(request, 'worker_register.html', {'user_form': user_form, 'worker_form': worker_form})


def customer_register(request):
    user_form = LoginRegister()
    customer_form = CustomerRegister()
    if request.method == 'POST':
        user_form = LoginRegister(request.POST)
        customer_form = CustomerRegister(request.POST,request.FILES)
        if user_form.is_valid() and customer_form.is_valid():
            user = user_form.save(commit=False)
            user.is_customer = True
            user.save()
            customer = customer_form.save(commit=False)
            customer.user = user
            customer.files=request.FILES['photo']
            customer.save()
            messages.info(request, 'Registered Successfully')
            return redirect('login')
    return render(request, 'customer_register.html', {'user_form': user_form, 'customer_form': customer_form})


def logout_view(request):
    logout(request)
    return redirect('login')


