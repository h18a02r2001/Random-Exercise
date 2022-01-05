from typing import ContextManager
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        "variable":"Harshit Singhal Sent you a text Message"
    }
    return render(request, 'index.html', context)
   # return HttpResponse("This is homepage")

def about(request):
    return render(request, 'about.html')
   # return HttpResponse("This is about Page")

def services(request):
    return render(request, 'services.html')
   # return HttpResponse("This is Services Page")

def contact(request):
    return render(request, 'contact.html')
   # return HttpResponse("This is Contact Page")
