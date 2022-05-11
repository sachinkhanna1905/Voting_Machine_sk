from django.shortcuts import redirect, render
from django.http import HttpResponse

# we need to import forms before using 
# from Poll_App.forms import CreatePollForm
# we also need to import models or schema
from Poll_App.models import Poll


# Create your views here.
def home(request):
    polls=Poll.objects.all()
    context ={
        'polls':polls
    }
    return render(request,'home.html',context)


def result(request,poll_id):
    poll=Poll.objects.get(pk=poll_id)
    context ={
        'poll':poll
    }
    return render(request,'result.html',context)

def vote(request,poll_id):
    poll= Poll.objects.get(pk=poll_id)

    if request.method=='POST':
        selected = request.POST['poll']
        print (selected)
        if selected=='question_one':
            question_one_count +=1
            (question_one_count).save()
        elif selected=='question_two':
            question_two_count +=1
            (question_two_count).save()
        elif selected=='question_three':
            question_three_count +=1
            (question_three_count).save()
        else:
            return HttpResponse(400,'Invalid form')
        
        poll.save()
        return redirect('results',poll.id)
    context={
        'poll':poll
    }
    return render(request,'vote.html',context)

def next(request):
    return render(request,'next.html')

def ok(request):
    return render(request,'ok.html')