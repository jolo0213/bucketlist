from django.contrib import admin
from blist.models import BL, Item, SharedList

class ItemInline(admin.TabularInline):
	model = Item
	extra = 5

class SharedInline(admin.TabularInline):
	model = SharedList

class BucketAdmin(admin.ModelAdmin):
	fieldsets = [('List Properties',{'fields':['name','owner']})]
	inlines = [ItemInline, SharedInline]
	search_fields = ['name']

# Register your models here.
admin.site.register(BL, BucketAdmin)
admin.site.register(Item)
admin.site.register(SharedList)