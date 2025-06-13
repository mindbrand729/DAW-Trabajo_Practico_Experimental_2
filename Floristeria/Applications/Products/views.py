from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *

# Create your views here.
class ProductsCreateView(CreateView):
    model = Products
    template_name = 'products.html'
    fields = '__all__'