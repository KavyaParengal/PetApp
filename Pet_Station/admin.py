from django.contrib import admin
from Pet_Station.models import Categories,PetData,Food,Notifications

# Register your models here.

admin.site.register(Categories)

admin.site.register(PetData)

admin.site.register(Food)

admin.site.register(Notifications)


