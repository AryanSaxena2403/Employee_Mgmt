from django.shortcuts import render,redirect
from django.http import HttpResponse
from emp.models import Emp
# Create your views here.

def home(request):
    # return HttpResponse("Student Home Page")
    emp=Emp.objects.all()
    return render(request,"home.html",{'emp':emp})
def add_emp(request):
    if request.method == "POST":
        name=request.POST.get('name')
        empid=request.POST.get('id')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        working=request.POST.get('working')
        department=request.POST.get('department')
        en=Emp( name=name,emp_id=empid,phone=phone,address=address,department=department)
        if working is None:
            en.working = False
        else:
            en.working=True
        en.save()
        return redirect("/emp/home/")
    return render(request,"add_emp.html",{})

def delete_emp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    emp.delete()
    return redirect("/emp/home/")
def update_emp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    return render(request,"update_emp.html",{
        'emp':emp
    })
def do_update_emp(request,emp_id):
    if request.method=='POST':
        name=request.POST.get('name')
        empid=request.POST.get('id')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        working=request.POST.get('working')
        department=request.POST.get('department')
        print(emp_id)

        en = Emp.objects.get(pk=emp_id)
        en=Emp( name=name,emp_id=empid,phone=phone,address=address,department=department)
        if working is None:
            en.working = False
        else:
            en.working=True
        en.save()

    return redirect("/emp/home")
