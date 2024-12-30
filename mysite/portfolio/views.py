from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to the Index Page!")
def month_view(request):
    months_dict = {
        "jan": "This is January",
        "feb": "This is February",
        "mar": "This is March",
        "apr": "This is April",
        "may": "This is May",
        "jun": "This is June",
        "jul": "This is July",
        "aug": "This is August",
        "sep": "This is September",
        "oct": "This is October",
        "nov": "This is November",
        "dec": "This is December",
    }
    return render(request, "portfolio/months.html", {"months": months_dict})

