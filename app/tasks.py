#
from celery import shared_task

# @shared_task
# def light_task():
#     print("=-==------------hey")


# @shared_task
# def heavy_task():
#     print("=======================heyo ")

from rabbitmq_instances.celery import app_1, app_2


@app_1.task
def light_task():
    print("=-==------------hey")


#
#
@app_2.task
def heavy_task():
    print("=======================heyo ")
