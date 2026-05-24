from django.db import models

# 1. Kategori Barang (Misal: Serat, Benang, Kain Mentah, Kain Jadi, Zat Kimia)
class Kategori(models.Model):
    nama_kategori = models.CharField(max_length=100)
    deskripsi = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nama_kategori

# 2. Satuan Ukur (Misal: Kg, Meter, Liter, Roll, Cone)
class Satuan(models.Model):
    nama_satuan = models.CharField(max_length=50) # Contoh: Kilogram
    simbol = models.CharField(max_length=10)      # Contoh: Kg

    def __str__(self):
        return f"{self.nama_satuan} ({self.simbol})"

# 3. Master Data Barang (Menyimpan SEMUA barang, dari serat kapas sampai kain gulungan)
class Barang(models.Model):
    # Pilihan tipe barang
    TIPE_BARANG = [
        ('BAHAN_BAKU', 'Bahan Baku (Serat/Kimia)'),
        ('WIP', 'Setengah Jadi (Benang/Greige)'),
        ('PRODUK_JADI', 'Kain Jadi (Roll)'),
    ]

    kode_barang = models.CharField(max_length=50, unique=True, help_text="Contoh: KTN-C30S-BLK")
    nama_barang = models.CharField(max_length=200, help_text="Contoh: Kain Katun Combed 30s Hitam")
    kategori = models.ForeignKey(Kategori, on_delete=models.RESTRICT)
    tipe = models.CharField(max_length=20, choices=TIPE_BARANG)
    
    # Menghubungkan ke Satuan
    satuan_utama = models.ForeignKey(Satuan, on_delete=models.RESTRICT)
    
    # Detail Spesifik Tekstil
    warna = models.CharField(max_length=100, blank=True, null=True)
    ukuran_atau_gsm = models.CharField(max_length=100, blank=True, null=True, help_text="Ketebalan kain/benang")
    
    # Harga
    harga_modal = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    harga_jual = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    
    # Kapan data ini dibuat
    tanggal_dibuat = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.kode_barang}] {self.nama_barang}"