from django.shortcuts import render

from home.forms import BookingForm
from .models import departments,doctors
from .forms import BookingForm
# Create your views here.
def home(request):
    return render(request, 'home.html')
  

def about(request):

     return render(request, 'about.html')

def booking(request):
     if request.method== "POST":
          form = BookingForm(request.POST)
          if form.is_valid():
               form.save()
               
     form = BookingForm()
     form_dict={
          'form' : form
     }
     return render(request, 'booking.html',form_dict)

def doctor(request):
     doct_dict={
          'doct':doctors.objects.all()
     }
     return render(request, 'doctors.html',doct_dict)

def contact(request):
     return render(request, 'contact.html')

def department(request):
    dept_dict= { 'dept' : departments.objects.all()}
    return render(request, 'departments.html',dept_dict)