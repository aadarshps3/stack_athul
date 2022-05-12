from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import cv2
import numpy as np
import face_recognition
import os

from homeservice_app.forms import FeedbackForm, PayBillForm
from homeservice_app.models import Worker, Schedule, Customers, Appointment, Feedback, Bill, CreditCard


@login_required(login_url='login_view')
def customer_home(request):
    return render(request, 'customertemp/customer_home.html')


@login_required(login_url='login_view')
def view_workers_customer(request):
    data = Worker.objects.all()
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

def facepay(request):
    path = 'media/Training_images'
    images = []
    classNames = []
    myList = os.listdir(path)
    print(myList)
    for cl in myList:
        curImg = cv2.imread(f'{path}/{cl}')
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])
    print(classNames)
    print(type(classNames))
    encodeList = []

    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


    encodeListKnown = facepay(images)
    print('Encoding Complete')

    cap = cv2.VideoCapture(0)

    while True:
        success, img = cap.read()
        # img = captureScreen()
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            print(faceDis)
            matchIndex = np.argmin(faceDis)
            print(matchIndex)

            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
                # print(name)
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                # if (label == 0):
                #     num = 'MY'
                #     value = write_read(num)
                #     break
                # elif (label == 1):
                #     num = 'NM'
                #     value = write_read(num)
                #     break

        cv2.imshow('Webcam', img)
        if cv2.waitKey(1) == ord("q"):
            break






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
