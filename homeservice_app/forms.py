import re

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from homeservice_app.models import Login, Nursery, Farmer, Work, Officer, Feedback, Chat, upload_img , Addproduct , upload_imgg , weather,seed,plant,fertilizer


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'
    


def phone_number_validator(value):
    if not re.compile(r'^[7-9]\d{9}$').match(value):
        raise ValidationError('This is Not a Valid Phone Number')


class LoginRegister(UserCreationForm):
    username=forms.CharField()
    password1=forms.CharField(widget=forms.PasswordInput,label='password')
    password2=forms.CharField(widget=forms.PasswordInput,label='confirm password')

    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2')


class NurseryRegister(forms.ModelForm):
    phone_number = forms.CharField(validators=[phone_number_validator])

    class Meta:
        model = Nursery
        fields = ('owner_name', 'nursery_name', 'email', 'address','phone_number', 'nursery_regid')


class FarmerRegister(forms.ModelForm):
    contact_no = forms.CharField(validators=[phone_number_validator])

    class Meta:
        model = Farmer
        fields = ('name', 'contact_no', 'email', 'address','photo','Adhar_id')

class OfficerRegister(forms.ModelForm):
    contact_no = forms.CharField(validators=[phone_number_validator])

    class Meta:
        model = Officer
        fields = ('name', 'contact_no', 'email', 'address','office_location','office_name','photo','id_card')

class Workform(forms.ModelForm):
    class Meta:
        model = Work
        fields = '__all__'


# class SchdeuleForm(forms.ModelForm):
#     date = forms.DateField(widget=DateInput)
#     start_time = forms.TimeField(widget=TimeInput, )
#     end_time = forms.TimeField(widget=TimeInput, )
#
#     class Meta:
#         model = Schedule
#         fields = ( 'date', 'start_time', 'end_time')
#
#
# class AddBill(forms.ModelForm):
#     # name = forms.ModelChoiceField(queryset=Customers.objects.filter(role='customer'))
#
#     class Meta:
#         model = Bill
#         exclude = ('status', 'paid_on')
#
#
# class PayBillForm(forms.ModelForm):
#     card_no = forms.CharField(validators=[RegexValidator(regex='^.{16}$', message='Please Enter a Valid Card No')])
#     card_cvv = forms.CharField(widget=forms.PasswordInput,
#                                validators=[RegexValidator(regex='^.{3}$', message='Please Enter a Valid CVV')])
#     expiry_date = forms.DateField(widget=DateInput(attrs={'id': 'example-month-input'}))
#
#     class Meta:
#         model = CreditCard
#         fields = ('card_no', 'card_cvv', 'expiry_date')
#
#
class FeedbackForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    class Meta:
        model = Feedback
        fields = ('subject', 'Enquiry', 'date')

class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ('desc',)

class upload_form(forms.ModelForm):

    class Meta:
        model=upload_img
        fields=['img_upload']

class upload_form1(forms.ModelForm):

    class Meta:
        model=upload_imgg
        fields=['soil']


class Stock(forms.ModelForm):
    class Meta:
        model = Addproduct
        fields = ('product_name','price','photo')


class weatherform(forms.ModelForm):
    current_date = forms.DateField(widget=DateInput)
    predict_date = forms.DateField(widget=DateInput)
    class Meta:
        model = weather
        fields = ('current_date','predict_date','type','description')

class seedform(forms.ModelForm):
    class Meta:
        model= seed
        fields=('name','photo','rate','how_to_plant','duration')

class plantform(forms.ModelForm):
    class Meta:
        model=plant
        fields=('name','photo','rate','how_to_plant','duration')

class fertilizerform(forms.ModelForm):
    class Meta:
        model=fertilizer
        fields=('name','category','photo','rate','company_name','how_to_use')