from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.
from homeservice_app.forms import LoginRegister, NurseryRegister, FarmerRegister, OfficerRegister


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
            elif  user.is_nursery:
                return redirect('worker_home')
            elif  user.is_farmer:
                return redirect('farmerviewprofile')
            elif user.is_officer:
                return redirect('officer_home')
        else:
            messages.info(request, 'Invalid Credentials')
    return render(request, 'login.html')


def Nursery_register(request):
    user_form = LoginRegister()
    Nursery_form = NurseryRegister()
    if request.method == 'POST':
        user_form = LoginRegister(request.POST)
        Nursery_form = NurseryRegister(request.POST, request.FILES)
        if user_form.is_valid() and Nursery_form.is_valid():
            user = user_form.save(commit=False)
            user.is_nursery = True
            user.save()
            Nursery = Nursery_form.save(commit=False)
            Nursery.user = user
            Nursery.save()
            messages.info(request, 'Registered Successfully')
            return redirect('login_view')
    return render(request, 'worker_register.html', {'user_form': user_form, 'Nursery_form': Nursery_form})


def farmer_register(request):
    user_form = LoginRegister()
    customer_form = FarmerRegister()
    if request.method == 'POST':
        user_form = LoginRegister(request.POST)
        customer_form = FarmerRegister(request.POST,request.FILES)
        if user_form.is_valid() and customer_form.is_valid():
            user = user_form.save(commit=False)
            user.is_farmer = True
            user.save()
            customer = customer_form.save(commit=False)
            customer.user = user
            customer.files=request.FILES['photo']
            customer.save()
            messages.info(request, 'Registered Successfully')
            return redirect('login_view')
    return render(request, 'customer_register.html', {'user_form': user_form, 'customer_form': customer_form})


def officer_register(request):
    user_form = LoginRegister()
    officer_form = OfficerRegister()
    if request.method == 'POST':
        user_form = LoginRegister(request.POST)
        officer_form = OfficerRegister(request.POST, request.FILES)
        if user_form.is_valid() and officer_form.is_valid():
            user = user_form.save(commit=False)
            user.is_officer = True
            user.save()
            officer = officer_form.save(commit=False)
            officer.user = user
            officer.save()
            messages.info(request, 'Registered Successfully')
            return redirect('view_officer')
    return render(request, 'officertemp/reg.html', {'user_form': user_form, 'officer_form': officer_form})





def logout_view(request):
    logout(request)
    return redirect('login_view')


