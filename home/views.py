from django.shortcuts import render
from .models import departments,doctors
# Create your views here.
def home(request):
    return render(request, 'home.html')
  

def about(request):
     return render(request, 'about.html')

def booking(request):

    return render(request, 'booking.html')

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