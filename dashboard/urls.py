from django.urls import path
from . import views

urlpatterns = [
    path('salaries', views.dashboard_with_pivot, name='dashboard_with_pivot'),
    path('inflation', views.dashboard_inflation, name='dashboard_inflation'),
    path('data', views.pivot_data, name='pivot_data'),
    path('inflation_data', views.inflation_data, name='inflation_data'),
]