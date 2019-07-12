from django.contrib import admin
from .models import Product, SizeProduct, Bill, Detail
from django.utils.html import format_html
from django.utils.safestring import mark_safe

class SizeInLine(admin.StackedInline):
    model = SizeProduct
    extra = 1

class ImageAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="150" height="150" />'.format(obj.photo.url))
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
    fields = ('image_tag', 'name', 'photo','ingredients')
    readonly_fields = ('image_tag',)
    list_display = ('name','ingredients')
    inlines = [SizeInLine]

admin.site.register(Product, ImageAdmin)

class BillInLine(admin.StackedInline):
    model = Detail
    extra = 0

class BillAdmin(admin.ModelAdmin):
    inlines = [BillInLine]

admin.site.register(Bill, BillAdmin)