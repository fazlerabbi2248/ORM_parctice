from django.urls import path
from .views import *
from . import views



urlpatterns = [
   path('', views.student_list_OR, name='student_data'),


]