from django.db import connection
from django.shortcuts import render

# Create your views here.
from chapter5.models import StudentParent
from student.models import Student


# How to model one to one relationships?

def student_list_OR(request):
    student = Student.objects.get(surname='khan')
    p1 = StudentParent(student=student, father_name='Vilasrao Deshmukh', mother_name='Vaishali Deshmukh')
    p1.save()
    studentparent = StudentParent.objects.all()

    return render(request, 'index.html',{'posts':studentparent})