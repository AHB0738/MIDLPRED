from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/predict/', views.api_predict, name='api_predict'),  # Cette ligne doit exister
    path('clear-history/', views.clear_history, name='clear_history'),
    path('about/', views.about, name='about'),
]