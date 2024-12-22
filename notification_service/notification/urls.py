from django.urls import path
from .views import trigger_email

urlpatterns = [
    path('trigger-email/', trigger_email, name='trigger_email'),
]
