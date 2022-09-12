from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import cv2
import numpy as np
import face_recognition
import os
from homeservice_app.prediction import model_predict
from homeservice_app.prediction1 import model_predict1

from homeservice_app.forms import FeedbackForm, ChatForm , upload_form,upload_form1,FarmerRegister
from homeservice_app.models import Nursery, Farmer, Feedback, Chat , upload_img,Addproduct ,upload_imgg,seed,plant,fertilizer


def customer_home(request):
    return render(request, 'customertemp/customer_home.html')



def farmerviewprofile(request):
    farmer = Farmer.objects.get(user=request.user)
    return render(request, 'customertemp/profileview.html',{'farmer': farmer})


def updatefarmer(request):
    farmer = Farmer.objects.get(user=request.user)
    form = FarmerRegister(instance=farmer)
    if request.method == 'POST':
        form = FarmerRegister(request.POST, instance=farmer)
        if form.is_valid():
            form.save()
            messages.info(request, ' Profile Updated Successfully')
            return redirect('farmerviewprofile')
    return render(request, 'customertemp/update.html', {'form': form})


@login_required(login_url='login_view')
def view_workers_customer(request):
    data = Nursery.objects.all()
    return render(request, 'customertemp/workers.html', {'data': data})

def view_Nursery1(request):
    data = Nursery.objects.all()
    return render(request, 'customertemp/workers.html', {'data': data})


@login_required(login_url='login_view')
def view_schedule_customer(request):
    s = Schedule.objects.all()
    context = {
        'schedule': s
    }
    return render(request, 'customertemp/schedule_view.html', context)


@login_required(login_url='login_view')
def take_appointment(request, id):
    s = Schedule.objects.get(id=id)
    c = Customers.objects.get(user=request.user)
    appointment = Appointment.objects.filter(user=c, schedule=s)
    if appointment.exists():
        messages.info(request, 'You Have Already Requested Appointment for this Schedule')
        return redirect('view_schedule')
    else:
        if request.method == 'POST':
            obj = Appointment()
            obj.user = c
            obj.schedule = s
            obj.save()
            messages.info(request, 'Appointment Booked Successfully')
            return redirect('appointment_view')
    return render(request, 'customertemp/take_appointment.html', {'schedule': s})


@login_required(login_url='login_view')
def appointment_view(request):
    c = Customers.objects.get(user=request.user)
    a = Appointment.objects.filter(user=c)
    return render(request, 'customertemp/appointment_view.html', {'appointment': a})


@login_required(login_url='login_view')
def Feedback_add_user(request):
    form = FeedbackForm()
    u = request.user
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = u
            obj.save()
            messages.info(request, 'Complaint Registered Successfully')
            return redirect('Feedback_view_user')
    return render(request, 'customertemp/complaint_add.html', {'form': form})


@login_required(login_url='login_view')
def Feedback_view_user(request):
    f = Feedback.objects.filter(user=request.user)
    return render(request, 'customertemp/complaint_view.html', {'feedback': f})


def view_bill_user(request):
    u = Customers.objects.get(user=request.user)
    print(u)
    bill = Bill.objects.filter(name=u)
    print(bill)
    return render(request, 'customertemp/view_bill_user.html', {'bills': bill})


def pay_bill(request, id):
    bi = Bill.objects.get(id=id)
    form = PayBillForm()
    if request.method == 'POST':
        card = request.POST.get('card')
        c = request.POST.get('cvv')
        da = request.POST.get('exp')
        CreditCard(card_no=card, card_cvv=c, expiry_date=da).save()
        bi.status = 1
        bi.save()
        messages.info(request, 'Bill Paid  Successfully')
        return redirect('bill_history')

        # form = PayBillForm(request.POST)
        # if form.is_valid():
        #     pay = form.save(commit=False)
        #     pay.bill = bi
        #     pay.save()
        #     bi.status = 1
        #     bi.save()

    return render(request, 'customertemp/view_bill_user.html', )


def pay_in_direct(request, id):
    bi = Bill.objects.get(id=id)
    bi.status = 2
    bi.save()
    messages.info(request, 'Choosed to Pay Fee Direct in office')
    return redirect('bill_history')


def bill_history(request):
    u = Customers.objects.get(user=request.user)
    bill = Bill.objects.filter(name=u, status__in=[1, 2])

    return render(request, 'customertemp/view_bill_history.html', {'bills': bill})


# def successful(request):
#     return render(request, 'successfull.html',)

def chat_add(request):
    form = ChatForm()
    u = request.user
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = u
            obj.save()
            messages.info(request, 'Complaint Registered Successfully')
            return redirect('chat_add')
    else:
        form = ChatForm()
    return render(request,'customertemp/chat_add.html',{'form':form})

def chat_view(request):
    print('hi')
    chat = Chat.objects.all()
    print(chat)
    return render(request,'customertemp/chat_view.html',{'chat':chat})

def task_load(request):

    return render(request,'customertemp/TASK.html')


def load_upload_page(request):
    if request.method =="POST" and 'upload_btn' in request.POST:

        form = upload_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.error(request, "Image Uploaded Sucessfully!")
        else:
            form = upload_form()
            messages.error(request, "Image not Uploaded!")

    if request.method =="POST" and 'check_btn' in request.POST:

       obj=upload_img.objects.all().last()
       scr=obj.img_upload
       new_scr='media/'+str(scr)
       print("___________the scourse _----------- ")
       print(new_scr)
       get_prediction=model_predict(new_scr)
       print("____________ the prediction ______________")
       print(get_prediction)
       context={
           "image":obj,
           "prediction":get_prediction
                }
       return render(request, 'customertemp/choose.html',context)

    if request.method == "POST" and 'log_out_btn' in request.POST:

        return redirect('log_out_load')


    return render(request,'customertemp/choose.html')



def task_load1(request):

    return render(request,'customertemp/TASKK.html')


def load_upload_page1(request):
    if request.method =="POST" and 'upload_btn' in request.POST:

        form = upload_form1(request.POST,request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            messages.error(request, "Image Uploaded Sucessfully!")
        else:
            form = upload_form1()
            messages.error(request, "Image not Uploaded!")

    if request.method =="POST" and 'check_btn' in request.POST:

       obj=upload_imgg.objects.all().last()
       scr1=obj.soil
       new_scr='media/'+str(scr1)
       print("___________the scourse _----------- ")
       print(new_scr)
       get_prediction=model_predict1(new_scr)
       print("____________ the prediction ______________")
       print(get_prediction)
       context={
           "image":obj,
           "prediction":get_prediction
                }
       return render(request, 'customertemp/choosee.html',context)

    if request.method == "POST" and 'log_out_btn' in request.POST:

        return redirect('log_out_load')


    return render(request,'customertemp/choosee.html')


def view_stock1(request):
    data = seed.objects.all()
    data1 = plant.objects.all()
    data2 = fertilizer.objects.all()
    return render(request, 'customertemp/view_stock.html', {'data': data,'data1':data1,'data2':data2})