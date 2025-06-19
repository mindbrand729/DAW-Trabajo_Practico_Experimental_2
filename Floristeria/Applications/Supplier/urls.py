from django.urls import path
from .views import SupplierListView, SupplierDetailView, SupplierCreateView, SupplierUpdateView, SupplierDeleteView

urlpatterns = [
    path('', SupplierListView.as_view(), name='supplier_list'),
    path('<int:pk>/', SupplierDetailView.as_view(), name='supplier_detail'),
    path('create/', SupplierCreateView.as_view(), name='supplier_create'),
    path('update/<int:pk>/', SupplierUpdateView.as_view(), name='supplier_update'),
    path('delete/<int:pk>/', SupplierDeleteView.as_view(), name='supplier_delete'),
]
