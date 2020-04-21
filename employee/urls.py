from django.urls import path
from . views import *

urlpatterns = [
    path("",views.employee_list, name='employee_list'),
    path("<int:id>/details/",views.employee_details,name='employee_details'),
]
