from django.urls import path
from . import views

urlpatterns = [
    path('invoice/<int:so_id>/', views.cetak_invoice, name='cetak_invoice'),
]