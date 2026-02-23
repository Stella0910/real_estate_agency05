from django.contrib import admin


from property.models import Flat, Complaint, Owner


class FlatsInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ['owner']


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address']
    readonly_fields = ['created_at']
    list_display = [
        'address',
        'price',
        'new_building',
        'construction_year',
        'town'
    ]
    list_editable = ['new_building']
    list_filter = [
        'new_building',
        'rooms_number',
        'has_balcony',
        'active',
    ]
    raw_id_fields = ['liked_by']
    inlines = [
        FlatsInline,
    ]


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['user', 'flat']


class OwnerAdmin(admin.ModelAdmin):
    search_fields = ['name', 'pure_phone']
    raw_id_fields = ['flats']
    list_display = ['name', 'pure_phone']


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
