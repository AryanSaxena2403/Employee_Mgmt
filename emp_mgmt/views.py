from django.http import HttpResponse
from django.shortcuts import render
import datetime

def home(request):
   
    return render(request,"home.html")
def about(request):
    print('This is abt page')
    return HttpResponse('This is abt page')

