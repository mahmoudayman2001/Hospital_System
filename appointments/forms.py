
from django import forms
from .models import Doctor , Appoinment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from datetime import date , datetime

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        
        fields = [
        'name', 
        'mobile',
        'specialty',
        ]


class AppoinmentForm(forms.ModelForm):

    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'min': date.today().strftime('%Y-%m-%d')})
    )


    class Meta :
        model = Appoinment

        fields = [
            'name',
            'doctor',
            'date',
            'time',
            'duration'
        ]   

        widgets = {
            'date' : forms.DateInput(attrs={'type': 'date'}),
             

         }


class SignupForm(UserCreationForm):
    email = forms.EmailField()

    class Meta :
        model = User
        fields = ('email', 'username', 'password1', 'password2')
