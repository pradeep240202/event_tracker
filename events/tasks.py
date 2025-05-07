# tasks.py in your app (e.g., events)

from celery import shared_task
import logging

# Set up logging
logger = logging.getLogger(__name__)

@shared_task
def notify_new_event(event_id):
    logger.info(f"New event received: {event_id}")
    result = f"Notification sent for event: {event_id}"
    print(result)
    return result
