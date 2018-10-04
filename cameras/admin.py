from django.contrib import admin
from .models import Company, Brand, Type, Product, Collection
from django.contrib.auth.models import User


class ProductAdmin(admin.ModelAdmin):
    list_display =  ('name',    'modelNumber', 'releasedDate',    'insertDate')
    list_filter =  ('releasedDate',    'insertDate')
    search_fields = ('name',    'modelNumber')

    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
    #     if request.user.is_superuser:
    #         return qs
    #     return qs.filter(user=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            kwargs["queryset"] = User.objects.filter(id=request.user.id)

        return super().formfield_for_foreignkey(db_field, request, **kwargs)






class ProductInline(admin.TabularInline):
    model = Product

class BrandAdmin(admin.ModelAdmin):
    inlines = [
        ProductInline,
    ]

admin.site.register(Company)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Collection)
admin.site.register(Type)
# Register your models here.
