from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('vice_versa', views.vice_versa, name='vice_versa'),
    path('reverse', views.reverse, name='reverse'),
]
