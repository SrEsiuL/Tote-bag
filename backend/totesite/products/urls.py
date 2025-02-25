from django.urls import path
from . import views

urlpatterns = [
    path('totes/', views.totebag_list, name='totebag_list'),
    path('contact/', views.contact, name='contact'),
]