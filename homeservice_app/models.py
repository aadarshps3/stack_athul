from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Login(AbstractUser):
    is_worker = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)


class Work(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    charge = models.IntegerField()

    def __str__(self):
        return self.name


class Worker(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE, related_name='worker')
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField(max_length=200)
    work_type = models.ForeignKey(Work, on_delete=models.CASCADE)
    id_card = models.ImageField(upload_to='id_cards')

    def __str__(self):
        return self.name


class Customers(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE, related_name='customer')
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField(max_length=200)
    photo=models.ImageField(upload_to="Training_images",unique=True)

    def __str__(self):
        return self.name




class Bill(models.Model):
    name = models.ForeignKey(Customers, on_delete=models.CASCADE)
    bill_date = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    paid_on = models.DateField(auto_now=True)
    status = models.IntegerField(default=0)


class CreditCard(models.Model):
    card_no = models.CharField(max_length=30)
    card_cvv = models.CharField(max_length=30)
    expiry_date = models.CharField(max_length=200)


class Schedule(models.Model):
    employee = models.ForeignKey(Worker, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()


class Appointment(models.Model):
    user = models.ForeignKey(Customers, on_delete=models.CASCADE, related_name='appointment')
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)


class Feedback(models.Model):
    user = models.ForeignKey(Login, on_delete=models.DO_NOTHING)
    subject = models.CharField(max_length=200)
    feedback = models.TextField()
    date = models.DateField()
    reply = models.TextField(null=True, blank=True)
