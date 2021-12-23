from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('export/', views.export, name='export'),
    path('details/', views.details, name='details'),
    path('details-new/', views.details_new, name='details-new'),
    

]