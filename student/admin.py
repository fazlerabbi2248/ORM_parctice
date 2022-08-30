from django.contrib import admin

from . import models
from .models import Student,Teacher

# Register your models here.

admin.site.register(models.Student)
admin.site.register(models.Teacher)
admin.site.register(models.Hero)
admin.site.register(models.Category)