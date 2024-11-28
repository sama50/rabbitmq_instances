#
from celery import shared_task

# @shared_task
# def light_task():
#     print("=-==------------hey")


# @shared_task
# def heavy_task():
#     print("=======================heyo ")

from celery import shared_task


@shared_task
def light_task():
    print("=-==------------hey")


#
#
@shared_task
def heavy_task():
    print("=======================heyo ")
