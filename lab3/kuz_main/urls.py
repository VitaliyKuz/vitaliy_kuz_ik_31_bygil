from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='kuz_main'),
    path('health/', views.health, name='health')
]