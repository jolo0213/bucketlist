from django.contrib import admin
from blist.models import BL, Item

class ItemInline(admin.TabularInline):
	model = Item
	extra = 5

class BucketAdmin(admin.ModelAdmin):
	fieldsets = [('List Properties',{'fields':['_name']})]
	inlines = [ItemInline]
	search_fields = ['bl_name']

# Register your models here.
admin.site.register(BL, BucketAdmin)
admin.site.register(Item)