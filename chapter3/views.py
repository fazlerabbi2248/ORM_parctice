from django.db.models.functions import Lower
from django.shortcuts import render


from student.models import Student, Category, Hero

# Create your views
# How to create multiple objects in one shot?
"""
def student_list_OR(request):

    categorys = Category.objects.all()
    Category.objects.bulk_create(
        [Category(name="God"),
         Category(name="Demi God"),
         Category(name="Mortal")])

    categorys = Category.objects.all()
    print(categorys.count())




    print(categorys )



    # print(str(students.query))

    return render(request, 'index.html',{'posts':categorys})
"""
#  How to copy or clone an existing model object?
"""
def student_list_OR(request):

    categorys = Category.objects.all()
    heros =  Hero.objects.all().count()
    print(heros)
    heros =   Hero.objects.first()
    heros.pk = None
    heros.save()
    print(heros)

    return render(request, 'index.html',{'posts':categorys})
"""
# How to convert string to datetime and store in database?

# parse_date(date_str) is used for convert string date
# method 2
# temp_date = datetime.strptime(date_str, "%Y-%m-%d").date()


# chapter 4
#  How to order a queryset in ascending or descending order?

def student_list_OR(request):

    students = Student.objects.all().order_by('-age','surname')

    print(students.count())

# How to order a queryset in case insensitive manner?

    students = Student.objects.all().order_by(Lower('surname')).values_list('surname', flat=True)

# 4 How to order on a field from a related model (with a foreign key)?
    students = Hero.objects.all().order_by('category__name', 'name').values_list('name')

    print(students )



    print(str(students.query))

    return render(request, 'index.html',{'posts':students})