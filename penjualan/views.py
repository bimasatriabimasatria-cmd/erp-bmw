from django.shortcuts import get_object_or_404
from .models import SalesOrder
from .utils import render_to_pdf

def cetak_invoice(request, so_id):
    so = get_object_or_404(SalesOrder, id=so_id)
    return render_to_pdf('penjualan/invoice.html', {'so': so})