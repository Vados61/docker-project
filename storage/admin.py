from django.contrib import admin

from storage.models import Client, FireExtingusher, Order, Position, Firm


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['firm', 'adress']


@admin.register(FireExtingusher)
class FireExtingusherAdmin(admin.ModelAdmin):
    list_display = ['type', 'weight', 'repair_coast']


class QuantityInline(admin.TabularInline):
    model = Position
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['owner', 'status', 'date_input']
    inlines = [QuantityInline]


@admin.register(Firm)
class Firm(admin.ModelAdmin):
    list_display = ['name']
