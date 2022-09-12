from django.contrib import admin
from homeservice_app import models
# Register your models here.


admin.site.register(models.Login)
admin.site.register(models.Nursery)
admin.site.register(models.Farmer)
admin.site.register(models.Work)
admin.site.register(models.Chat)
# admin.site.register(models.Bill)
# admin.site.register(models.Schedule)