from django.db import models

# Create your models here.
from student.models import Student


class StudentParent(models.Model):
    student = models.OneToOneField(Student,on_delete=models.CASCADE,primary_key=True,)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)

class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='reporter')
    def __str__(self):
        return self.headline
    class Meta:
        ordering = ('headline',)
