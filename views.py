from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

monthly_challenge = {
    "january": "Eat no meat for the entire month!",
    "february" : "Walk for atleast 20 minutes every day!",
    "march": "Learn Django for atleast 20 minutes daily!",
    "april": "Eat no meat for the entire month!",
    "may": "Drink more water" ,
    "june": "Love yourself",
    "july": "Live for the sake of Allah",
    "august": "Walk for atleast 20 minutes every day!",
    "september": "Clean the house",
    "octobar": "Learn something new",
    "november": "Eat no meat for the entire month!",
    "december": None
}

# Create your views here.

def index(request):
    months = list(monthly_challenge.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenge.keys())
    
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    
    redirect_months = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_months])
    return HttpResponseRedirect(redirect_path)

def monthly_challenges(request, month):
    try:
        challenge_text = monthly_challenge[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month
        })
    except:
        raise Http404
    