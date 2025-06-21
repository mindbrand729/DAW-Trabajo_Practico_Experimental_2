"""
URL configuration for Floristeria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('Applications.home.urls')),
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('company/', CompanyCreateView.as_view()),
    path('employee/', EmployeeCreateView.as_view()),
    path('products/', ProductsCreateView.as_view()),
    path('supplier/', SupplierCreateView.as_view()),
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('suppliers/', include('Applications.Supplier.urls')), # Incluye las URLs de tu app Supplier
]
=======
    path('company/', include('Applications.Company.urls')),
    path('employee/', include('Applications.Employee.urls')),
    path('products/', include('Applications.Products.urls')),
    path('supplier/', include('Applications.Supplier.urls')),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> 67f13f0a598c9036664f6c8669c4cc71168b80e8
