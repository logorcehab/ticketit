from django.contrib import admin
from .models import Cart, Ticket, Events
# Register your models here.

admin.site.register(Cart)
admin.site.register(Ticket)
admin.site.register(Events)