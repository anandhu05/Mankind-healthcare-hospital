from logging import PlaceHolder
from django import forms
from matplotlib import widgets

from .models import booking

class DateInput(forms.DateInput):
    input_type='date'



class BookingForm(forms.ModelForm):
    class Meta:
        model=booking
        fields="__all__"
        widgets={'booking_date':DateInput(),
                
        }
        labels={
            'patient_name':'Patient Name',
            'patient_phno': 'Phone Number',
            'doctor': 'Select your Doctor',
            'booking_date':'Preferred Appointment Date'
            
        }
