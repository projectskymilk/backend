from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class IndexView(TemplateView):
    template_name = 'milksky/index.html'

def reportPage(request):
    context = {}
    return render(request, "milksky/reports.html", context)