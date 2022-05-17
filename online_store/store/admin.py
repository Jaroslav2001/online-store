from django.contrib import admin

from store.models import (
    Category,
    Product,
    PropertiesKey,
    PropertiesValue,
)

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(PropertiesKey)
admin.site.register(PropertiesValue)
