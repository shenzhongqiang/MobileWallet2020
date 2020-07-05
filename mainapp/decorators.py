from django.urls import reverse
from .models import Usage
from mainapp.views import *

def record_usage(view_func):
    def wrapper(request, *args, **kwargs):
        usage = Usage(api_func=view_func.__name__, user=request.user)
        usage.save()
        return view_func(request, *args, **kwargs)
    return wrapper
