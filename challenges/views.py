from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
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
    'december': 'Have your first detty christmas'

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
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound('This Month is not supported')
