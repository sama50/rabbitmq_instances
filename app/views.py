from django.http import HttpResponse
from .tasks import heavy_task, light_task

def handle_request(request):
    # Dispatch a heavy task
    heavy_task.delay()

    # Dispatch a light task
    light_task.delay()

    return HttpResponse("Tasks dispatched!")
