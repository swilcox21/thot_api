from django.contrib import admin
from api.models import Reminder
# Register your models here.

class ReminderAdmin(admin.ModelAdmin):
    readonly_fields = ['id']
    list_display = ['id','owner','text','created_date']
    ordering = ['owner','created_date']


admin.site.register(Reminder, ReminderAdmin)