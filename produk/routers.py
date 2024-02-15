# Menggunakan Router untuk mengarahkan query
# Anda perlu menentukan cara Django akan membagi query antara dua basis data.
# Ini dapat dilakukan dengan membuat Router khusus

class MyRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == "produk":
            return "secondary"
        return "default"
    
    def db_for_write(self, model, **hints):
        if model._meta.app_label == "produk":
            return "secondary"
        return "default"
    
    def allow_relation(self, obj1, obj2, **hints):
        if (obj1._meta.app_label == "produk" or
            obj1._meta.app_label == "produk"
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == "produk":
            return db == "secondary"
        return db == "default"
