from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Employee

# Create your views here.
class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee_list.html'
    context_object_name = 'employees'

class EmployeeDetailView(ListView):
    model = Employee
    template_name = 'employee_detail.html'
    context_object_name = 'employees'

    def get_queryset(self):
        Idemployee = 4
        return Employee.objects.filter(id=Idemployee)


class EmployeeCreateView(CreateView):
    model = Employee
    template_name = 'employee_form.html'
    fields = '__all__'
    success_url = '/employee'

class EmployeeUpdateView(UpdateView):
    model = Employee
    template_name = 'employee_formup.html'
    fields = '__all__'
    context_object_name = 'Upemployee'
    success_url = '/employee'
    

class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'employee_delete.html'
    success_url = '/employee'
    context_object_name = 'delemployee'  
