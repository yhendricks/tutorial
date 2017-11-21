from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import HomeForm

# Create your views here.
#def home(request):
 #   return HttpResponse('It works')


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request):
        form = HomeForm()
        return render(request, self.template_name, {'form': form})
