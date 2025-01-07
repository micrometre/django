from django.http import HttpResponse
from django.utils import timezone


def index(request):
    now = timezone.now()
    print(now)
    print(request.headers)     # HTTP headers
    return HttpResponse("Hello, world. You're at the polls index.")