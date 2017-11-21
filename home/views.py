from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
def home(request):
    return HttpResponse('It works')


class HomeView(TemplateView):
    template_name = 'home/home.html'