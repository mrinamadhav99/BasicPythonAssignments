from django.urls import path
from . import views

urlpatterns = [
    path('months/', views.month_view, name='month_view'),
    path('portfolio/','portfolio.urls')
]
