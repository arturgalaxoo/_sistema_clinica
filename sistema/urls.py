# São as importações realizadas de forma a utilizar partes do django.
from django.urls import path
# Importação do módulo views.py, onde tem a view index e a view listarPacientes
from sistema import views

app_name = 'sistema'

# Lista reponsável por organizar as urls do sistema.
urlpatterns = [
    path('', views.index, name='index'),
    path('pacientes/', views.listarPacientes, name='pacientes'),
    path('medicos/', views.listarMedicos, name ='medicos'),
]

