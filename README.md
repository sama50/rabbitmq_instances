To start particular celery 
celery -A rabbitmq_instances.celery.app_1 worker --loglevel=DEBUG 
celery -A rabbitmq_instances.celery.app_2 worker --loglevel=DEBUG 
