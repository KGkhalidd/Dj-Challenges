from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

monthly_challenges = {
    'january': 'Eat no meat for the entire month!',
    'february': 'study django for the entire month!',
    'march': 'play football!',
    'april': 'Eat no meat for the entire month!',
    'may': 'study django for the entire month!',
    'june': 'play football!',
    'july': 'Eat no meat for the entire month!',
    'august': 'study django for the entire month!',
    'september': 'play football!',
    'october': 'Eat no meat for the entire month!',
    'november': 'study django for the entire month!',
    'december': 'play football!',
}


def monthly_challenges_by_number(request, month):
    # made a list of keys'months' in the dict
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound('Invalid Month!')

    # pass the number that we take from the request as index to the months
    # now redirect_month = the string of the month that we want
    redirect_month = months[month-1]

    # made a dynamic path , so if u change the path he will get it automatically
    # the first attr is the name in the path in urls
    redirect_path = reverse(
        'month-challenge', args=[redirect_month])  # challenge/january

    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):

    try:
        challenge_text = monthly_challenges[month]
        response_data = f'<h1>{challenge_text}</h2>'
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound('This month is not supported!')

    
