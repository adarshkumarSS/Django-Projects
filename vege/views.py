from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required   
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model
#from vege.seed import generate_report_card

#CUSTOM USER MODEL
# User = get_user_model()

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

def update_receipe(request,slug):
    queryset = receipes.objects.get(slug = slug)
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
        
    return render(request ,'login.html')

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

def student_login(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.error(request, "Invalid Username")
            return redirect('/student_login/')
        
        user = authenticate(username = username, password = password)

        if user is None:
            messages.error(request, "Invalid Password")
            return redirect('/student_login/')
        else:
            login(request , user)
            return redirect('/students/')
        
    return render(request ,'report/student_login.html')

def student_logout(request):
    logout(request)
    return redirect('/student_login/')

def student_register(request):
    if request.method == "POST":
        first_name=request.POST.get('first_name' ,None)
        last_name=request.POST.get('last_name' , None)
        username=request.POST.get('username' , None)
        password=request.POST.get('password' , None)

        
        if not first_name:
            messages.error(request, "first name required")
            return redirect('/student_register/')
        elif not last_name:
            messages.error(request, "last name required")
            return redirect('/student_register/')
        elif not username:
            messages.error(request, "username required")
            return redirect('/student_register/')
        elif not password:
            messages.error(request, "Password required")
            return redirect('/student_register/')
        
        

        user=User.objects.filter(username = username)
        if user.exists():
            messages.error(request, "Username Exists")
            return redirect('/student_register/')
        user = User.objects.create(
            first_name =first_name,
            last_name = last_name,
            username = username
        )
        user.set_password(password)
        user.save()
        messages.success(request, "Account created successfully")
        return redirect('/student_register/')
    return render(request,'report/student_register.html')

from django.db.models import Q,Sum

def get_students(request):
    queryset = Student.objects.all().order_by('student_id')
    search_query = request.GET.get('search', '')
    if request.GET.get('search'):
        search = request.GET.get('search')
        queryset = queryset.filter(
            Q(student_name__icontains = search) |
            Q(department__department__icontains = search) |
            Q(student_id__student_id__icontains = search) |
            Q(student_email__icontains = search) |
            Q(student_age__icontains = search) 
      
        )
        

    paginator = Paginator(queryset, 10) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
 

    context = {
        'page_obj': page_obj,
        'search_query': search_query,
        'queryset' : page_obj
    }
    print(context)
    return render(request, 'report/students.html' ,context )



def see_marks(request , student_id):
    #generate_report_card()
    detail = Student.objects.filter(student_id__student_id = student_id)
    queryset = SubjectMarks.objects.filter(student__student_id__student_id = student_id)
    total_marks = queryset.aggregate(total_marks = Sum('marks'))
    #current_rank = -1
    #ranks = Student.objects.annotate(marks = Sum('studentmarks__marks')).order_by('-marks')
    #i=1
    #for rank in ranks:
        #if student_id == rank.student_id.student_id:
            #current_rank= i
            #break
        #i= i+1

    return render(request, 'report/see_marks.html' ,{'queryset':queryset , 
                                                    'total_marks':total_marks , 
                                                    'detail':detail ,} )

