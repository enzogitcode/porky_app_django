from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView, DeleteView

# Create your views here.
def home(request):
    return render(request, 'home.html')
# class Home(TemplateView):
#     template_name= 'home.html'

def about(request):
    return render(request, 'about.html')

class ListBooks(ListView):
    pass
