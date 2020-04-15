from django.shortcuts import render
from . models import *
from django.http import Http404

def index(request):
    question = Question.objects.all()
    context = {"question":question,"title":"Poll"}
    return render(request,'polls/index.html',context)

def details(request,id=None):
    try:
        question = Question.objects.get(id=id)
    except:
        raise Http404
    context = {"question":question}
    return render(request,'polls/details.html',context)
