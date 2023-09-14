from django.contrib import admin

from Outsider.models import Log,outsiders,Cart,OrderAddress,chat

# Register your models here.

admin.site.register(Log)

admin.site.register(outsiders)

admin.site.register(Cart)

admin.site.register(OrderAddress)

admin.site.register(chat)

