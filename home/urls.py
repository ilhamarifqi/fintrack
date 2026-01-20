from django.urls import path
from . import views  # Nah, di SINI baru kita import views dari folder yang sama

urlpatterns = [
    path('', views.index, name='index'),

]