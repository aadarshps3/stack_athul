from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Login(AbstractUser):
    is_nursery = models.BooleanField(default=False)
    is_farmer = models.BooleanField(default=False)
    is_officer = models.BooleanField(default=False)


class Work(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    charge = models.IntegerField()

    def __str__(self):
        return self.name


class Nursery(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE, related_name='worker')
    owner_name = models.CharField(max_length=100)
    nursery_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    address = models.TextField(max_length=200)
    nursery_regid = models.TextField(max_length=200)

    def __str__(self):
        return self.nursery_name


class Farmer(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE, related_name='customer')
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField(max_length=200)
    photo=models.ImageField(upload_to="Photo",unique=True)
    Adhar_id = models.ImageField(upload_to="images", unique=True)

    # def __str__(self):
    #     return self.name

class Officer(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE, related_name='officer')
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField(max_length=200)
    office_regno = models.CharField(max_length=25)
    office_location = models.CharField(max_length=25)
    office_name = models.CharField(max_length=25)
    photo=models.ImageField(upload_to="oPhoto",unique=True)
    id_card = models.ImageField(upload_to="oimages", unique=True)

    def __str__(self):
        return self.name




# class Bill(models.Model):
#     name = models.ForeignKey(Farmer, on_delete=models.CASCADE)
#     bill_date = models.DateTimeField(auto_now_add=True)
#     amount = models.IntegerField()
#     paid_on = models.DateField(auto_now=True)
#     status = models.IntegerField(default=0)
#
#
# class CreditCard(models.Model):
#     card_no = models.CharField(max_length=30)
#     card_cvv = models.CharField(max_length=30)
#     expiry_date = models.CharField(max_length=200)
#
#
# class Schedule(models.Model):
#     employee = models.ForeignKey(Worker, on_delete=models.CASCADE)
#     date = models.DateField()
#     start_time = models.TimeField()
#     end_time = models.TimeField()
#
#
# class Appointment(models.Model):
#     user = models.ForeignKey(Farmer, on_delete=models.CASCADE, related_name='appointment')
#     schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
#     status = models.IntegerField(default=0)
#
#
class Feedback(models.Model):
    user = models.ForeignKey(Login, on_delete=models.DO_NOTHING)
    subject = models.CharField(max_length=200)
    Enquiry = models.TextField()
    date = models.DateField()
    reply = models.TextField(null=True, blank=True)

class Chat(models.Model):
    user = models.ForeignKey(Login,on_delete=models.CASCADE,related_name='farmer',null=True)
    desc = models.TextField()

class upload_img(models.Model):
    img_upload=models.ImageField(upload_to='uploads')

class upload_imgg(models.Model):
    soil=models.ImageField(upload_to='soil')

class Addproduct(models.Model):
    user = models.ForeignKey(Nursery,on_delete=models.CASCADE,null=True)
    product_name = models.CharField(max_length=200)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='nursery')


class weather(models.Model):
    current_date=models.DateField()
    predict_date=models.DateField()
    type = models.CharField(max_length=40)
    description = models.CharField(max_length=200)

class seed(models.Model):
    user=models.ForeignKey(Nursery,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=20)
    photo=models.ImageField(upload_to='seed')
    rate=models.IntegerField(max_length=5)
    how_to_plant=models.CharField(max_length=250)
    duration=models.CharField(max_length=10)

class plant(models.Model):
    user=models.ForeignKey(Nursery,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=20)
    photo=models.ImageField(upload_to='plant')
    rate=models.IntegerField(max_length=5)
    how_to_plant=models.CharField(max_length=250)
    duration=models.CharField(max_length=10)

class fertilizer(models.Model):
    user=models.ForeignKey(Nursery,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=20)
    category=models.IntegerField(max_length=5)
    photo = models.ImageField(upload_to='fertilizer')
    rate=models.IntegerField(max_length=5)
    company_name=models.CharField(max_length=50)
    how_to_use=models.CharField(max_length=250)
