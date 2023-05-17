from django.urls import path , include
from . import views
from .views import signup


urlpatterns = [

     path(
        "new/",
        views.DoctorCreateView.as_view(),
        name="Doctor-create"
        ),

    path(
        "Doctor-list/",
        views.Doctorslistview.as_view(),
        name="Doctor-list"
),

    path(
        "appoinment/",
        views.AppointmentCreateView.as_view(),
        name="Appoinment-create"
        ),

    path(
        "appoinment-list",
        views.Appoinmentlistview.as_view(),
        name="Appoinment-list"
),    

    path(
        'doctor/<int:pk>/',
        views.DoctorDetailView.as_view(),
        name="doctor-appointments"
),    
    path("", signup , name="signup") , 

    path("accounts/", include("django.contrib.auth.urls")),

   
]
