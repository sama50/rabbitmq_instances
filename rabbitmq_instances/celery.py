from celery import Celery
import os

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rabbitmq_instances.settings')

# Initialize the first Celery app with its own broker
app = Celery('rabbitmq_instances')
app.conf.broker_url = 'amqp://guest:guest@127.0.0.1:5555/'  # First RabbitMQ instance
app.autodiscover_tasks()  # Replace with your actual app name





