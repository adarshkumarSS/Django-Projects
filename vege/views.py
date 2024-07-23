from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required   
from django.core.paginator import Paginator
# Create your views here.
@login_required(login_url="/login/")
def receipe(request):  # sourcery skip: extract-method
    
    if request.method == "POST":
        data = request.POST
        receipi_image = request.FILES.get('receipi_image')
        receipi_name = data.get('receipi_name')
        receipi_description = data.get('receipi_description')
        
        receipes.objects.create(
            receipi_image = receipi_image,
            receipi_name = receipi_name,
            receipi_description = receipi_description,

        )
        return redirect('/receipe/')
    queryset=receipes.objects.all()
   
    if request.GET.get('search'):
        queryset = queryset.filter(receipi_name__icontains = request.GET.get('search'))

    context = {'receipe': queryset}
    return render(request,'receipe.html', context)

@login_required(login_url="/login/")

def update_receipe(request,id):
    queryset = receipes.objects.get(id = id)
    context = {'receipes': queryset}

    if request.method == "POST":
        data = request.POST

        receipi_image = request.FILES.get('receipi_image')
        receipi_name = data.get('receipi_name')
        receipi_description = data.get('receipi_description')
        
        queryset.receipi_name = receipi_name
        queryset.receipi_description = receipi_description
        
        if receipi_image:
            queryset.receipi_image = receipi_image
             
        queryset.save()
        return redirect('/receipe/')

    return render(request,'update_receipe.html', context)

@login_required(login_url="/login/")
def delete_receipe(request,id):
    queryset = receipes.objects.get(id = id)
    queryset.delete()
    return redirect('/receipe/')

def login_page(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.error(request, "Invalid Username")
            return redirect('/login/')
        
        user = authenticate(username = username, password = password)

        if user is None:
            messages.error(request, "Invalid Password")
            return redirect('/login/')
        else:
            login(request , user)
            return redirect('/receipe/')
        
    return render(request , 'login.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')




def register(request):
    if request.method == "POST":
        first_name=request.POST.get('first_name' ,None)
        last_name=request.POST.get('last_name' , None)
        username=request.POST.get('username' , None)
        password=request.POST.get('password' , None)

        
        if not first_name:
            messages.error(request, "first name required")
            return redirect('/register/')
        elif not last_name:
            messages.error(request, "last name required")
            return redirect('/register/')
        elif not username:
            messages.error(request, "username required")
            return redirect('/register/')
        elif not password:
            messages.error(request, "Password required")
            return redirect('/register/')
        
        

        user=User.objects.filter(username = username)
        if user.exists():
            messages.error(request, "Username Exists")
            return redirect('/register/')
        user = User.objects.create(
            first_name =first_name,
            last_name = last_name,
            username = username
        )
        user.set_password(password)
        user.save()
        messages.success(request, "Account created successfully")
        return redirect('/register/')
    return render(request,'register.html')

def get_students(request):
    queryset = Student.objects.all()

    if request.GET.get('search'):
        search = request.GET.get('search')
        queryset = queryset.filter(student_name__icontains = search)

    paginator = Paginator(queryset, 10) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    print(page_obj)
    return render(request, 'report/students.html' ,{'queryset':page_obj})