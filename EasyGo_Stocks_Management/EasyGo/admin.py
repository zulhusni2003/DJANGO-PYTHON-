from django.contrib import admin

# Register your models here.
from .models import Staff, Product, FaQ, FaQ_management,Stock_management

admin.site.register(Staff)
admin.site.register(Product)
admin.site.register(FaQ)
admin.site.register(FaQ_management)
admin.site.register(Stock_management)


