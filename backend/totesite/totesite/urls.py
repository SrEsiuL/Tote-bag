from django.contrib import admin
from django.urls import path, include
from products.views import home  

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('api/', include('products.urls')),  
    path('', home, name='home'),  
]