from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Company

# Create your views here.
class CompanyListView(ListView):
    model = Company
    template_name = 'company_list.html'
    context_object_name = 'company'

class CompanyDetailView(DetailView):
    model = Company
    template_name = 'company_detail.html'
    context_object_name = 'company'

class CompanyCreateView(CreateView):
    model = Company
    template_name = 'company_form.html'
    fields = '__all__'
    success_url = reverse_lazy('company_list')

class CompanyUpdateView(UpdateView):
    model = Company
    template_name = 'company_form.html'
    fields = '__all__'
    success_url = reverse_lazy('company_list')

class CompanyDeleteView(DeleteView):
    model = Company
    template_name = 'company_delete.html'
    success_url = reverse_lazy('company_list')   
