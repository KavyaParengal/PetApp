from django.contrib import admin

from Outsider.models import Log,outsiders,Cart,OrderAddress,chat,Favorite,Order,payment

# Register your models here.

admin.site.register(Log)

admin.site.register(outsiders)

admin.site.register(Cart)

admin.site.register(OrderAddress)

admin.site.register(chat)

admin.site.register(Favorite)

admin.site.register(Order)

admin.site.register(payment)

