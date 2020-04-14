from django.shortcuts import render
from . models import *

def index(request):
    question = Question.objects.all()
    context = {"question":question,"title":'Poll'}
    return render(request,'polls/index.html',context)