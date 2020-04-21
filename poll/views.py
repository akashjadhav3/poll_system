from django.shortcuts import render
from . models import *
from django.http import Http404,HttpResponse

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

def poll(request, id=None):
    if request.method == "GET":
        try:
            question = Question.objects.get(id=id)
        except:
            raise Http404
        context = {"question":question}
        return render(request, 'polls/poll.html',context)
    if request.method=="POST":
        user_id = 1
        data = request.POST
        ret = Answer.objects.create(user_id = user_id, choice_id=data['choice'])
        if ret:
            return HttpResponse("Your vote Done Successfully!!")
        else:
            return HttpResponse("Your vote Not Done successfully")