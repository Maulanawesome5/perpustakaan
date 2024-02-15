from django.core.serializers.json import DjangoJSONEncoder
from datetime import datetime


class CustomJSONEncoder(DjangoJSONEncoder):
    """Menggunakan custom serializer saat dumpdata
    `python manage.py dumpdata produk.buku
    --database=default
    --exclude=contenttypes
    --indent 2
    --format custom_json > "data/produk.buku.json"`
    """
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)
