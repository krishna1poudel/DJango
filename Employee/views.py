from django.shortcuts import render


# Create your views here.

from django.http import HttpResponse


def index(request):
    return render(request,'base.html')


def employee(request):
    return render(request, 'Employee.html')

def employeer(request):
 
    return render(request,'employeer.html')