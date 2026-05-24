from django.apps import AppConfig

class ProduksiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'produksi'

    def ready(self):
        import produksi.signals  # <--- TAMBAHKAN INI