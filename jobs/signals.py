from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import JobApplication
from accounts.models import Notification

@receiver(post_save, sender=JobApplication)
def send_application_notification(sender, instance, created, **kwargs):
    if created:
        job = instance.job
        employer = job.employer
        Notification.objects.create(
            user=employer,
            title="New Applicant Received",
            message=f"You have received a new application for '{job.title}'."
        )
