from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Customer)
class customer(admin.ModelAdmin):
    list_display = ['name','email','accbal']

@admin.register(Transfer)
class Transfer(admin.ModelAdmin):
    list_display = ['sender','reciever','date_tran']

