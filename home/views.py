from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')
  

def about(request):
     return render(request, 'about.html')

def booking(request):

    return render(request, 'booking.html')

def doctor(request):
     
     return render(request, 'doctor.html')

def contact(request):
     return render(request, 'contact.html')

def department(request):
     
    return render(request, 'department.html')