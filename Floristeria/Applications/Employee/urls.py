from django.urls import path
from .views import EmployeeListView, EmployeeDetailView, EmployeeCreateView, EmployeeUpdateView, EmployeeDeleteView

urlpatterns = [
    path('', EmployeeListView.as_view(), name='employee_list'),
    path('detalle/', EmployeeDetailView.as_view(), name='employee_detail'),
    path('create/', EmployeeCreateView.as_view(), name='employee_create'),
    path('update/<pk>/', EmployeeUpdateView.as_view(), name='employee_update'),
    path('delete/<pk>/', EmployeeDeleteView.as_view(), name='employee_delete'),
]
