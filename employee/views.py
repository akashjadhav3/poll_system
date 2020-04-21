from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse
from employee.forms import UserForm

def employee_list(request):
    context={"users":User.objects.all(),"title":"Employee"}
    return render(request,'employee/index.html',context)

def employee_details(request,id=None):
    context = {"user":get_object_or_404(User,id=id)}
    return render(request,'employee/details.html',context)
    