from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    peoples=[
        {'name':'adarsh','age':12},
        {'name':'mithles','age':18},
        {'name':'chaitanya','age':3},
        {'name':'surya','age':63}
    ]
    for people in peoples:
        if people['age'] :
            print("yes")
    vegetables={'pumpkin','tomato','potato'}
    return render(request,"home\index.html", context={'page':'Django Server','peoples':peoples,'veetables':vegetables})
def about(request):
    context = {'page' : 'about'}
    return render(request,"home/about.html", context)
def contact(request):
    context = {'page' : 'contact'}
    return render(request,"home/contact.html", context)
