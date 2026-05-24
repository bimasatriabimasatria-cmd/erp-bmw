from django.shortcuts import render
from inventaris.models import Stok
from penjualan.models import SalesOrder, SalesItem
from django.db.models import Sum, F
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required # Hanya yang login yang bisa akses
def index(request):
    # Cek apakah user adalah admin
    is_admin = request.user.is_superuser
    
    # ... (kode perhitungan stok & laba sebelumnya) ...
    
    context = {
        'stok': semua_stok,
        'jumlah_sales': total_sales,
        'is_admin': is_admin, # Kirim informasi ini ke HTML
    }
    return render(request, 'dashboard/index.html', context)

def index(request):
    # 1. Ringkasan Stok
    semua_stok = Stok.objects.all()
    
    # 2. Ringkasan Keuangan
    # Ambil semua item penjualan yang sudah selesai
    items_terjual = SalesItem.objects.filter(so__status='SELESAI')
    
    # Mari kita lihat ada berapa item yang terhitung di sistem (untuk debugging)
    jumlah_data = items_terjual.count()

    # Hitung Total Pendapatan = Jumlah * Harga Jual
    pendapatan = items_terjual.aggregate(total=Sum(F('jumlah') * F('harga_jual')))['total'] or 0
    
    # Hitung Total Modal = Jumlah * Harga Modal (diambil dari master data barang)
    modal = items_terjual.aggregate(total=Sum(F('jumlah') * F('barang__harga_modal')))['total'] or 0
    
    # Hitung Laba Bersih
    laba = pendapatan - modal
    
    context = {
        'stok': semua_stok,
        'pendapatan': pendapatan,
        'modal': modal,
        'laba': laba,
        'jumlah_data': jumlah_data,
    }
    return render(request, 'dashboard/index.html', context)