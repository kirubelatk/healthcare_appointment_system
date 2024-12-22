from celery import shared_task
from .models import NotificationLog

@shared_task
def send_email_notification(email, subject, message):
    try:
        # Simulate sending an email (replace with actual email logic)
        print(f"Sending email to {email}: {subject} - {message}")
        
        # Log the notification as sent
        NotificationLog.objects.create(
            email=email,
            subject=subject,
            message=message,
            status='Sent'
        )
    except Exception as e:
        # Log the notification as failed
        NotificationLog.objects.create(
            email=email,
            subject=subject,
            message=message,
            status='Failed'
        )
        raise e
