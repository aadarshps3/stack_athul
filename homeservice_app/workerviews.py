from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from homeservice_app.forms import Stock,seedform,plantform,fertilizerform
from homeservice_app.models import Farmer, Nursery , Addproduct,weather,seed,plant,fertilizer



def worker_home(request):
    return render(request, 'workertemp/worker_home.html')


@login_required(login_url='login_view')
def schedule_add(request):
    form = SchdeuleForm()
    if request.method == 'POST':
        form = SchdeuleForm(request.POST)
        if form.is_valid():
            form=form.save(commit=False)
            form.employee=Worker.objects.get(user=request.user)
            form.save()
            messages.info(request, 'schedule added successful')
            return redirect('schedule_views')
    return render(request, 'workertemp/schedule_add.html', {'form': form})


@login_required(login_url='login_view')
def schedule_view(request):
    u=Worker.objects.get(user=request.user)
    print(u)
    s = Schedule.objects.filter(employee=u)
    print(s)
    context = {
        'schedule': s
    }
    return render(request, 'workertemp/schedule_view.html', context)


@login_required(login_url='login_view')
def schedule_update(request, id):
    s = Schedule.objects.get(id=id)
    if request.method == 'POST':
        form = SchdeuleForm(request.POST or None, instance=s)
        if form.is_valid():
            form.save()
            messages.info(request, 'schdeule updated')
            return redirect('schedule_views')
    else:
        form = SchdeuleForm(instance=s)
    return render(request, 'workertemp/schedule_update.html', {'form': form})


@login_required(login_url='login_view')
def schedule_delete(request, id):
    s = Schedule.objects.filter(id=id)
    if request.method == 'POST':
        s.delete()
        return redirect('schedule_views')

def view_bill_worker(request):
    bill = Bill.objects.all()
    print(bill)
    return render(request, 'workertemp/view_payment_details.html', {'bills': bill})

@login_required(login_url='login_view')
def appointment_view_worker(request):
    a = Appointment.objects.all()
    return render(request, 'workertemp/appointment_view.html', {'appointment': a})


def stockpage(request):
    stock_form = Stock()
    if request.method == 'POST':
        stock_form = Stock(request.POST, request.FILES)
        if stock_form.is_valid():
            stock_form.save()
            messages.info(request, 'Prescription generated')
            return redirect(worker_home)
    return render(request,'workertemp/add_stock.html',{'stock_form': stock_form})


def view_stock(request):
    data = seed.objects.all()
    data1 = plant.objects.all()
    data2 = fertilizer.objects.all()
    return render(request, 'workertemp/view_stock.html', {'data': data,'data1':data1,'data2':data2})

def update_seed(request, id):
    data = seed.objects.get(id=id)
    form = seedform(instance=data)
    if request.method == 'POST':
        form = seedform(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('view_stock')
    return render(request, 'workertemp/update_stock.html', {'form': form})


def remove_seed(request, id):
    data = seed.objects.get(id=id)
    data.delete()
    return redirect('view_stock')

def update_plant(request, id):
    data = plant.objects.get(id=id)
    form = plantform(instance=data)
    if request.method == 'POST':
        form = plantform(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('view_stock')
    return render(request, 'workertemp/update_stock.html', {'form': form})


def remove_plant(request, id):
    data = plant.objects.get(id=id)
    data.delete()
    return redirect('view_stock')

def update_fertilizer(request, id):
    data = fertilizer.objects.get(id=id)
    form = fertilizerform(instance=data)
    if request.method == 'POST':
        form = fertilizerform(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('view_stock')
    return render(request, 'workertemp/update_stock.html', {'form': form})


def remove_fertilizer(request, id):
    data = fertilizer.objects.get(id=id)
    data.delete()
    return redirect('view_stock')


def seedpage(request):
    seed_form = seedform()
    if request.method == 'POST':
        seed_form = seedform(request.POST, request.FILES)
        if seed_form.is_valid():
            seed_form.save()
            messages.info(request, 'product added')
            return redirect(worker_home)
    return render(request,'workertemp/add_seed.html',{'seed_form': seed_form})


def plantpage(request):
    plant_form = plantform()
    if request.method == 'POST':
        plant_form = plantform(request.POST, request.FILES)
        if plant_form.is_valid():
            plant_form.save()
            messages.info(request, 'product added')
            return redirect(worker_home)
    return render(request,'workertemp/add_plant.html',{'plant_form': plant_form})


def fertilizerpage(request):
    fertilizer_form = fertilizerform()
    if request.method == 'POST':
        fertilizer_form = fertilizerform(request.POST, request.FILES)
        if fertilizer_form.is_valid():
            fertilizer_form.save()
            messages.info(request, 'product added')
            return redirect(worker_home)
    return render(request,'workertemp/add_fertilizer.html',{'fertilizer_form': fertilizer_form})

def weatherdetails2(request):
    data = weather.objects.all()
    return render(request,'workertemp/weathernursery.html',{'data':data})