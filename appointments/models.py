from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import date




class Doctor(models.Model):
        name = models.CharField(max_length=50)
        mobile = models.IntegerField(null=True)
        specialty = models.CharField(max_length=50)

        def __str__(self):
            return self.name






class Patient(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.IntegerField(null=True)

class Appoinment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    

    date = models.DateField(default=date.today)


    time = [
        ('08:00', '08:00'),
        ('08:15', '08:15'),
        ('08:30', '08:30'),
        ('08:45', '08:45'),
        ('09:00', '09:00'),
        ('09:15', '09:15'),
        ('09:30', '09:30'),
        ('09:45', '09:45'),
        ('10:00', '10:00'),
        ('10:15', '10:15'),
        ('10:30', '10:30'),
        ('10:45', '10:45'),
        ('11:00', '11:00'),
        ('11:15', '11:15'),
        ('11:30', '11:30'),
        ('11:45', '11:45'),
        ('12:00', '12:00'),
        ('12:15', '12:15'),
        ('12:30', '12:30'),
        ('12:45', '12:45'),
        ('13:00', '13:00'),
        ('13:15', '13:15'),
        ('13:30', '13:30'),
        ('13:45', '13:45'),
        ('14:00', '14:00'),
    ]
    time = models.CharField(choices=time, max_length=15 , default=None)
    booked = models.BooleanField(default=False)
    duration_choices = [
        (15, _("15 minutes")),
        (30, _("30 minutes")),
        (45, _("45 minutes")),
        (60, _("1 hour")),
    ]
    duration = models.IntegerField(choices=duration_choices, default=15)
    end_time = models.CharField(max_length=5, blank=True, null=True)
    
    def __str__(self):
        return self.name

    
    
    
        

    
    
    


   

