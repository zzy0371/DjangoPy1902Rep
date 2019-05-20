from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question,Choice
# Create your views here.
def index(request):
    questions = Question.objects.all()
    return render(request,'polls/index.html', locals())

def detail(request,id):
    question = Question.objects.get(pk = id)
    if request.method == "POST":
        c_id = request.POST["choice"]
        Choice.objects.incresevotes(c_id)

        return HttpResponseRedirect('/polls/result/%s/'%(id,))

    return render(request,'polls/detail.html', locals())

def result(request,id):
    question = Question.objects.get(pk=id)
    return render(request, 'polls/result.html', locals())