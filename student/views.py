from django.db import connection
from django.db.models import OuterRef, Subquery, F, Q, Avg, Max, Min, Sum, Count
from django.shortcuts import render
from .models import *



# Create your views here.

# all objects

"""

def student_list(request):
    # For getting all records
    posts = Student.objects.all()

    print(posts)
    print(posts.all())
    print(posts.query)
    print(connection.queries)
    print(str(posts.query))

    return render(request, 'index.html',{'posts':posts})

"""
"""
# Student list filter

def student_list_fiter(request):
    # For getting all records
    posts = Student.objects.filter(age__exact=23)

    print(posts)
    print(posts.all())
    print(posts.query)
    print(connection.queries)
    print(str(posts.query))

    return render(request, 'index.html',{'posts':posts})

"""
# OR Queries
"""
def student_list_OR(request):
    # For getting all records
    posts = Student.objects.filter(firstname__startswith='a') | Student.objects.filter(surname__startswith='k')



    print(posts)
    print(posts.all())
    print(posts.query)
    print(connection.queries)
    print(str(posts.query))

    return render(request, 'index.html',{'posts':posts})

"""
# AND queris

"""
def student_list_AND(request):
    # For getting all records
    # students = Student.objects.filter(firstname__startswith='f',surname__startswith='s')
    # using & operation

    students = Student.objects.filter(firstname__startswith='f') & Student.objects.filter(surname__startswith='s')





    print(students )


    # print(students .query)
   #  print(connection.queries)
    print(str(students .query))

    return render(request, 'index.html',{'posts':students})

"""
# Using Not : Two method
"""

def student_list_OR(request):
    # For getting all records
    # using Exclude

    # students = Student.objects.exclude(age__gte=24)
    # How to do union of two querysets from same or different models?
    students1 = Student.objects.exclude(age__gte=29)
    print(students1)
    student2 =Student.objects.filter(age__lt=24)
    print(student2)
    students = students1.union(student2)


    # students = Student.objects.filter(firstname__startswith='f') & Student.objects.filter(surname__startswith='s')





    print(students.count())


    # print(students .query)
   #  print(connection.queries)
    print(str(students .query))

    return render(request, 'index.html',{'posts':students})
"""

# How to select some fields only in a queryset?

"""
def student_list_OR(request):

    students = Student.objects.filter(firstname__startswith='f') & Student.objects.filter(surname__startswith='s').values('firstname','age')





    print(students )
    print(students.count())
    print(students.all().values())

    print(str(students .query))

    return render(request, 'index.html',{'posts':students})


"""
# 2.7 How to do a subquery expression in Django?
"""

def student_list_OR(request):
    hero_qs = Hero.objects.filter(category=OuterRef("pk")).order_by("-benevolence_factor")

    print(hero_qs )
   # print(hero_qs.count())


    print(str(hero_qs .query))

    return render(request, 'index.html',{'posts':hero_qs})

"""
# How to filter a queryset with criteria based on comparing their field values
"""
def student_list_OR(request):

    students = Student.objects.filter(firstname= F('surname'))





    print(students )
    print(students.count())
    print(students.all().values())

    print(str(students .query))

    return render(request, 'index.html',{'posts':students})

"""
#  How to use Q objects for complex queries?

"""
def student_list_OR(request):

    # students = Student.objects.filter(Q(firstname__endswith='i') | Q(surname__startswith='s'))
    students = Student.objects.filter(Q(firstname__endswith='i') & ~Q(surname__startswith='r'))





    print(students )
    print(students.count())
    print(students.all().values())

    print(str(students .query))

    return render(request, 'index.html',{'posts':students})
"""
# How to group records in Django ORM?

"""
def student_list_OR(request):

    students = Student.objects.all()
    totalstudents = Student.objects.all().aaggregate(Count('firstname'))
    print(totalstudents)
    avgage = Student.objects.all().aaggregate(Avg('age'))
    print(avgage)





    print(students )



    # print(str(totalstudents .query))

    return render(request, 'index.html',{'posts':students})
"""


# How to efficiently select a random object from a model?
def student_list_OR(request):

    students = Student.objects.all()

    print(students.count())




    print(students )



    # print(str(students.query))

    return render(request, 'index.html',{'posts':students})


# chapter 3 :


# How to create multiple objects in one shot?