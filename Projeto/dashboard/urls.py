from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('propor', views.propor_exercicio, name='propor_exercicio'),
    
    

]