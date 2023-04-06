from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here. Password - void loop

def index(request):
    context = {
        'variable':"Fuck You(I am Server)",
        'variable2':"Don't Show me Your Face(I am Server, your ex)"
    }
    return render(request, 'index.html', context)


def about(request):
    context2 = {
        'variable':"Fuck You(I am Server)",
        'variable2':"Don't Show me Your Face(I am Server, your ex)"
    }
    return render(request, 'about.html', context2)

def services(request):
   context3 = {
      'variable':"Fuck You(I am Server)",
      'variable2':"Don't Show me Your Face(I am Server, your ex)" 
   }
   return render(request, 'services.html', context3) 

def contact(request):
    if request.method == "POST":
        name =request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your Messeges Has Been Sent.')

    return render(request, 'contact.html')

