from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


monthly_challenges = {
    "january" : "Eat no meat!",
    "february" : "Walk for 20 mins every day!",
    "march" : "Learn English!",
    "april" : "Read a book!",
    "may" : "Learn Django!",
    "june" : "Consume no sugar!",
    "july" : "Learn HTML!",
    "august" : "drink no alcohol!",
    "september" : "Walk instead of Driving!",
    "october" : "Tell no lies!",
    "november" : "Face your fears!",
    "december" : "Listen to music!"
}

def index(request):
    list_items=""
    months = list(monthly_challenges.keys())
    
    for month in months:
        cpitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\" >{cpitalized_month}</a></li>"
        
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month_index):
    months = list(monthly_challenges.keys())
    if month_index > len(monthly_challenges):
        return HttpResponseNotFound("Invalid month!")
    redirect_month = months[month_index-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
        })
    except:
        return HttpResponseNotFound(f"<h2>{month} is not supported!</h2>")