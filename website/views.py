from django.urls import path
from . import views

urlpatterns = [
    path('', views.indx_viwe, name='index'),
]