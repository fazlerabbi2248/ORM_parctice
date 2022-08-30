from django.db import models

# Create your models here.

## How to ensure that only one object can be created?
from django.db.models import F


class Origin(models.Model):
    name = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)

# How to update denormalized fields in other models on save?

class CategoryCar(models.Model):
    name = models.CharField(max_length=100)
    hero_count = models.PositiveIntegerField()
    villain_count = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = "Categories"

class HeroCar(models.Model):
    name = models.CharField(max_length=100)
    CategoryCar = models.ForeignKey(CategoryCar, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.pk:
            CategoryCar.objects.filter(pk=self.CategoryCar_id).update(hero_count=F('hero_count')+1)
        super().save(*args, **kwargs)

class Villain(models.Model):
    name = models.CharField(max_length=100)
    categorycar = models.ForeignKey(CategoryCar, on_delete=models.CASCADE)

    def save(self,*args,**kwargs):
        if not self.pk:
            CategoryCar.objects.filter(pk=self.categorycar_id).update(villain_count=F('villain_count')+1)
        super().save(*args, **kwargs)


