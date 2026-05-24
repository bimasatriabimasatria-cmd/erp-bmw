from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import SalesOrder
from inventaris.models import Stok, TransaksiStok

@receiver(post_save, sender=SalesOrder)
def kurangi_stok_penjualan(sender, instance, created, **kwargs):
    if instance.status == 'SELESAI':
        for item in instance.items.all():
            # Kurangi stok
            stok = Stok.objects.get(barang=item.barang)
            stok.jumlah -= item.jumlah
            stok.save()
            
            # Catat Transaksi
            TransaksiStok.objects.create(
                barang=item.barang,
                jumlah=item.jumlah,
                tipe='KELUAR',
                catatan=f"Penjualan SO: {instance.nomor_so}"
            )