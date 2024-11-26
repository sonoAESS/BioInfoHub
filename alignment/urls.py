from django.urls import path
from .views import upload_sequence

urlpatterns=[
    path('upload/',upload_sequence, name='upload_sequence'),
]