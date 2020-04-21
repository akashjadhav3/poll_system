from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = "poll_list"),
    path('<int:id>/details/',views.details,name='poll_details'),
    path('<int:id>/',views.poll,name='single_poll'),
]
