from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import cv2
import numpy as np
import os

# from homeservice_app.forms import PayBillForm
from homeservice_app.models import Nursery, Farmer, Officer,Feedback,weather



def officer_home(request):
    return render(request,'officertemp/officer_home.html')

def remove_officer(request, id):
    data1 = Officer.objects.get(id=id)
    data = Login.objects.get(officer=data1)
    if request.method == 'POST':
        data.delete()
        return redirect('view_officer')
    else:
        return redirect('view_officer')

def Feedback_officer(request):
    f = Feedback.objects.all()
    return render(request, 'officertemp/complaint_view.html', {'feedback': f})

def view_Nursery3(request):
    data = Nursery.objects.all()
    return render(request, 'officertemp/workers.html', {'data': data})

def reply_Feedback(request, id):
    f = Feedback.objects.get(id=id)
    if request.method == 'POST':
        r = request.POST.get('reply')
        f.reply = r
        f.save()
        messages.info(request, 'Reply send for complaint')
        return redirect('Feedback_officer')
    return render(request, 'admintemp/reply_complaint.html', {'feedback': f})


def weatherdetails(request):
    data = weather.objects.all()
    return render(request,'officertemp/weatherofficer.html',{'data':data})