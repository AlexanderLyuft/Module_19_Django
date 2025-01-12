from django.urls import path
from task1.views import create_records

urlpatterns = [
    path('create_records/', create_records, name='create_records'),
]