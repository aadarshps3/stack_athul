from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


from homeservice_app.forms import Workform, LoginRegister, NurseryRegister,weatherform
from homeservice_app.models import Nursery, Login, Farmer, Work , Officer,weather



def admin_home(request):
    return render(request, 'admintemp/admin_home.html')


@login_required(login_url='login_view')
def view_Nursery(request):
    data = Nursery.objects.all()
    return render(request, 'admintemp/workers.html', {'data': data})


@login_required(login_url='login_view')
def workers_update(request, id):
    w = Worker.objects.get(id=id)
    l = Login.objects.get(worker=w)
    if request.method == 'POST':
        form = WorkerRegister(request.POST or None, instance=w)
        user_form = LoginRegister(request.POST or None, instance=l)
        if form.is_valid() and user_form.is_valid():
            form.save()
            user_form.save()
            messages.info(request, 'workers updated successful')
            return redirect('workers_view')
    else:
        form = WorkerRegister(instance=w)
        user_form = LoginRegister(instance=l)
    return render(request, 'admintemp/worker_update.html', {'form': form, 'user_form': user_form})


@login_required(login_url='login_view')
def remove_worker(request, id):
    data1 = Worker.objects.get(id=id)
    data = Login.objects.get(worker=data1)
    if request.method == 'POST':
        data.delete()
        return redirect('workers_view')
    else:
        return redirect('workers_view')


@login_required(login_url='login_view')
def view_customers(request):
    data = Farmer.objects.all()
    return render(request, 'admintemp/customers.html', {'data': data})


@login_required(login_url='login_view')
def remove_customers(request, id):
    data1 = Farmer.objects.get(id=id)
    data = Login.objects.get(customer=data1)
    if request.method == 'POST':
        data.delete()
        return redirect('customers_view')
    else:
        return redirect('customers_view')


@login_required(login_url='login_view')
def view_officer(request):
    data = Officer.objects.all()
    return render(request, 'admintemp/officers.html', {'data': data})

@login_required(login_url='login_view')
def remove_officer(request, id):
    data1 = Officer.objects.get(id=id)
    data = Login.objects.get(officer=data1)
    if request.method == 'POST':
        data.delete()
        return redirect('view_officer')
    else:
        return redirect('view_officer')


@login_required(login_url='login_view')
def add_work(request):
    if request.method == 'POST':
        form = Workform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('work_view')
    else:
        form = Workform()
    return render(request, 'admintemp/work_add.html', {'form': form})


@login_required(login_url='login_view')
def view_work(request):
    data = Work.objects.all()
    return render(request, 'admintemp/work.html', {'data': data})


@login_required(login_url='login_view')
def update_work(request, id):
    data = Work.objects.get(id=id)
    if request.method == 'POST':
        form = Workform(request.POST or None, instance=data)
        if form.is_valid():
            form.save()
            return redirect('work_view')
    else:
        form = Workform(request.POST or None, instance=data)
    return render(request, 'admintemp/work_update.html', {'form': form})


@login_required(login_url='login_view')
def delete_work(request, id):
    data = Work.objects.get(id=id)
    data.delete()
    return redirect('work_view')


@login_required(login_url='login_view')
def appointment_admin(request):
    a = Appointment.objects.all()
    context = {
        'appointment': a,
    }
    return render(request, 'admintemp/appointments.html', context)


@login_required(login_url='login_view')
def approve_appointment(request, id):
    a = Appointment.objects.get(id=id)
    a.status = 1
    a.save()
    messages.info(request, 'Appointment  Confirmed')
    return redirect('appointment_admin')


@login_required(login_url='login_view')
def reject_appointment(request, id):
    n = Appointment.objects.get(id=id)
    n.status = 2
    n.save()
    messages.info(request, 'Appointment Rejected')
    return redirect('appointment_admin')


@login_required(login_url='login_view')
def Feedback_officer(request):
    f = Feedback.objects.all()
    return render(request, 'admintemp/complaint_view.html', {'feedback': f})


@login_required(login_url='login_view')
def reply_Feedback(request, id):
    f = Feedback.objects.get(id=id)
    if request.method == 'POST':
        r = request.POST.get('reply')
        f.reply = r
        f.save()
        messages.info(request, 'Reply send for complaint')
        return redirect('Feedback_admin')
    return render(request, 'admintemp/reply_complaint.html', {'feedback': f})


def bill(request):
    form = AddBill()
    if request.method == 'POST':
        form = AddBill(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_bill')
    return render(request, 'admintemp/generate_bill.html', {'form': form})


def view_bill(request):
    bill = Bill.objects.all()
    print(bill)
    return render(request, 'admintemp/view_payment_details.html', {'bills': bill})



def weatherdata(request):
    form = weatherform()
    if request.method == 'POST':
        form = weatherform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_weather')
    return render(request,'admintemp/weather1.html' , {'form': form})

def view_weather(request):
    data = weather.objects.all()
    return render(request,'admintemp/view_temp.html',{'data':data})
