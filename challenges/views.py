from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


# Create your views here.


def index(request):
    months = list(monthly_challanges.keys())
    return render(request, "challenges/index.html",{
        "months": months
    })
  


monthly_challanges = {
    'january': 'Learn Everything about Django',
    'febuary': 'Learn how to be Organised',
    'march': 'Get better at Docker',
    'april': 'Get ready for school',
    'may': 'Build more applications',
    'june': 'Eat no meat for an entire month',
    'july': 'Travel to all your favourite places',
    'august': 'Pay it forward',
    'september': 'Have a glorious birthday',
    'october': 'Practice public speaking',
    'november': ' Write two certificate exams',
    'december': None

}


def monthly_challenge_by_number(request, month):
    months = list(monthly_challanges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid Month")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challange(request, month):
    try:
        challenge_text = monthly_challanges[month]
        return render(request,'challenges/challenge.html',{"text": challenge_text,
        "month": month,})
        
    except:
        raise Http404()
