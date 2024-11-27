from .celery import app_1 as celery_app
from .celery import app_2 as celery_app_1

__all__ = ("celery_app", "celery_app_1")
