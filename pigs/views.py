from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView, DeleteView

# Create your views here.

#con función
def home(request):
    return render(request, 'pigs/home.html')

#con class based views
# class Home(TemplateView):
#     template_name= 'home.html'

def about(request):
    return render(request, 'pigs/about.html')


