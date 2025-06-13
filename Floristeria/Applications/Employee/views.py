from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *

# Create your views here.
class EmployeeCreateView(CreateView):
    model = Employee
    template_name = 'employee.html'
    fields = '__all__'