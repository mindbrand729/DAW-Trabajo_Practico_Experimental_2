from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Products

# Create your views here.
class ProductsListView(ListView):
    model = Products
    template_name = 'products_list.html'
    context_object_name = 'products'

class ProductsDetailView(DetailView):
    model = Products
    template_name = 'products_detail.html'
    context_object_name = 'products'

class ProductsCreateView(CreateView):
    model = Products
    template_name = 'products_form.html'
    fields = '__all__'
    success_url = reverse_lazy('products_list')

class ProductsUpdateView(UpdateView):
    model = Products
    template_name = 'products_form.html'
    fields = '__all__'
    success_url = reverse_lazy('products_list')

class ProductsDeleteView(DeleteView):
    model = Products
    template_name = 'products_delete.html'
    success_url = reverse_lazy('products_list')  