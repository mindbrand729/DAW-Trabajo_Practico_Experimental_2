from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *

# Create your views here.
class SupplierCreateView(CreateView):
    model = Supplier
    template_name = 'supplier.html'
    fields = '__all__'