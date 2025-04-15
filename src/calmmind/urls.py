from django.urls import path
from .views import calmmindbot_response

urlpatterns = [
    path('', calmmindbot_response, name='calmmindbot'),
]
