from django.contrib import admin
from .models import Type,Company,Ticket,Response

# Register your models here.

class AdminCompany(admin.ModelAdmin):
    list_display = ['name']

class AdminType(admin.ModelAdmin):
    list_display = ['type']

class AdminTicket(admin.ModelAdmin):
    list_display = ['company','type','title']

class AdminResponse(admin.ModelAdmin):
    list_display = ['ticket','reply']


admin.site.register(Company,AdminCompany)
admin.site.register(Type,AdminType)
admin.site.register(Ticket, AdminTicket)
admin.site.register(Response, AdminResponse)
