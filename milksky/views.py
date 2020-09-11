from django.shortcuts import render
from django.views.generic import TemplateView
from datetime import datetime
from .models import ReportSignup

# Create your views here.
class IndexView(TemplateView):
    template_name = 'milksky/index.html'

class ReportsView(TemplateView):
    template_name = 'milksky/reports.html'

class AboutView(TemplateView):
    template_name = 'milksky/about.html'

def signupReport(request):
    newSignup = ReportSignup()
    newSignup.emailAddress = request.POST.get('email')
    newSignup.dateSignedUp = datetime.now()
    newSignup.save()
    context = {  
        'signedUp':"You're signed up!"  
            }
    return render(request, "milksky/reports.html", context)
