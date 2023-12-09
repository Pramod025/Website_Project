from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('details_form/',views.details_form, name='details_form'),
]

 