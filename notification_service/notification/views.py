from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .tasks import send_email_notification

def trigger_email(request):
    # Example data (replace with actual data if needed)
    email = "example@domain.com"
    subject = "Appointment Reminder"
    message = "This is a reminder for your upcoming appointment."

    # Trigger the Celery task
    send_email_notification.delay(email, subject, message)

    return JsonResponse({"status": "Notification sent!"})
