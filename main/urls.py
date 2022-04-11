from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('revers', views.revers, name='revers')
]
