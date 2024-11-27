from celery import Celery
import os

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rabbitmq_instances.settings')

# Initialize the first Celery app with its own broker
app_1 = Celery('rabbitmq_instances')
app_1.conf.broker_url = 'amqp://guest:guest@127.0.0.1:5672/'  # First RabbitMQ instance
app_1.autodiscover_tasks()  # Replace with your actual app name

# Initialize the second Celery app with a different broker
app_2 = Celery('rabbitmq_instances')
app_2.conf.broker_url = 'amqp://guest:guest@127.0.0.1:5673/'  # Second RabbitMQ instance
app_2.autodiscover_tasks()  # Replace with your actual app name

# Optionally, you can define task routes if needed
app_1.conf.task_routes = {
    'app.light_task': {'queue': 'light_queue'},
}

app_2.conf.task_routes = {
    'app.heavy_task': {'queue': 'heavy_queue'},
}


# from celery import Celery
# import os
#
# # Set the default Django settings module
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rabbitmq_instances.settings')
# # Initialize the first Celery app
# app_1 = Celery('rabbitmq_instances_1')
# app_1.conf.broker_url = 'amqp://guest:guest@127.0.0.1:5672/'
# app_1.conf.task_routes = {
#     'rabbitmq_instances.tasks.light_task': {'queue': 'light_queue'},
# }
# app_1.autodiscover_tasks()
# from kombu import Connection
# # Initialize the second Celery app
# app_2 = Celery('rabbitmq_instances_2')
# app_2.conf.broker_url = 'amqp://guest:guest@127.0.0.1:5673/'
# app_2.conf.task_routes = {
#     'rabbitmq_instances.tasks.heavy_task': {'queue': 'heavy_queue'},
# }
# app_2.autodiscover_tasks()



