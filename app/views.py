from django.shortcuts import render
from .models import Phonebook
from django.views.generic import ListView,CreateView,UpdateView,DeleteView

# Create your views here.
class ContactListView(ListView):
    model = Phonebook
    template_name = 'app/index.html'
    context_object_name = 'profiles'

class ContactCreateView(CreateView):
    model = Phonebook
    fields = '__all__'
