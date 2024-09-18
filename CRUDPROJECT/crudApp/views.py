from django.shortcuts import render,redirect
from .models import Student
from django.contrib import messages
from django.db.models import Q
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils import timezone

# Create your views here.

def home(request):
    data=Student.objects.filter(Isdelete=False)
    return render(request,'crudApp/home.html',{'data':data})

def contact(request):
    return render(request,'crudApp/contactUs.html')

def about(request):
    return render(request,'crudApp/about.html')

def form(request):
    if request.method=="POST":
        name=request.POST['name']
        age=request.POST['age']
        email=request.POST['email']
        message=request.POST['message']
        date=timezone.now()
        Student.objects.create(name=name,age=age,email=email,message=message)
        

        subject='python and Django'
        message=render_to_string('crudApp/msg.html',{'name':name,'date':date})
        from_email='dahalrohan82@gmail.com'
        recipient_list=[email]
        send_mail(subject,message,from_email,recipient_list,fail_silently=False)
        
        messages.success(request,f"Hi {name}!!Successfully Registered, check your Email")
        
        return redirect('form')
    return render(request,'crudApp/form.html')

def search(request):
    if request.method=="POST":
        searched=request.POST['searched']
        find=Student.objects.filter(Q(name__icontains=searched)|Q(message__icontains=searched)|Q(email__icontains=searched))
    return render(request,'crudApp/search.html',{'find':find})


def delete_data(request,id):
    std=Student.objects.get(id=id)
    std.Isdelete=True
    std.save()
    return redirect('home')

def update(request,id):
    data=Student.objects.get(id=id)
    if request.method=="POST":
        # name=request.POST.get('name')
        # age=request.POST.get('age')
        # email=request.POSST.get('email')
        # message=request.POST.get('message')

        # stu=Student.objects.get(id=id)
        # stu.name=name
        # stu.age=age
        # stu.email=email
        # stu.message=message
        # stu.save()
        stu=Student.objects.get(id=id)
        stu.name=request.POST.get('name')
        stu.age=request.POST.get('age')
        stu.email=request.POST.get('email')
        stu.message=request.POST.get('message')
        stu.save()  
        messages.success(request,"Successfully Updated")
        return redirect('home')
    return render(request,'crudApp/update.html',{'data':data})