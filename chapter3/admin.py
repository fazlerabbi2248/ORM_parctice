from django.contrib import admin

# Register your models here.
from chapter3 import models

admin.site.register(models.CategoryCar)
admin.site.register(models.Origin)
admin.site.register(models.Villain)
admin.site.register(models.HeroCar)