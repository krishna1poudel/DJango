from django.shortcuts import render


# Create your views here.

from django.http import HttpResponse


def index(request):
    return render(request,'base.html')


def employee(request):
    data=request.POST
    print(data)
    return render(request, 'Employee.html')

def employeer(request):
         context ={
             'name':"krishna poudel",
             'address':"sanepa,Lalitpur",
         }
         return render(request,'employeer.html',context)