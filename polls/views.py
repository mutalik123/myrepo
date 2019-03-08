from django.http import HttpResponse
#import sqlite3

from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
#from .forms import employee_form
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from .forms import data_form
from .models import TodoItem1


def signup(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:list')
    else:
        form=UserCreationForm()
    return render(request,'mypack/signup.html',{'form':form})

def login(request):
    if request.method=='POST':
        form =AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('articles:list')

    else:
        form=AuthenticationForm()
    return render(request,'mypack/login.html',{'form':form})



def employee(request):
    context = RequestContext(request)
    obj = TodoItem1.objects.all()
    print(obj)
    context_dict={}
    context_dict['obj']=obj
    return render(request,'mypack/adminpage.html',context_dict,context)

def enduser(request,*args,**kwargs):
    if request.method== 'POST':

        form=data_form(request.POST)
        if form.is_valid():
            try:
                Title = request.POST.get('title')
                description = request.POST.get('Description')
                date_time =request.POST.get('Date_And_time')
                status = request.POST.get('status')
                created_modified=request.POST.get('created and modified')
                print(Title)
                print(description)
                print(date_time)
                print(status)
                print(created_modified)
                TodoItem1.objects.create(Title=Title, description=description, date_time=date_time,status=status, created_modified=created_modified)
                return redirect("mypack:user")
            except Exception as e:
                raise
    else:
        form = data_form()
    return render(request,'mypack/nonuser.html',{"form": form })