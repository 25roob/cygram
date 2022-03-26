#Python
import pdb

# Django
from django.http import HttpResponse
from django.http import JsonResponse
from django.utils import timezone


def hello_world(request):
    now = timezone.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse(f'Oh, hi! Current server time is {now}')


def hi(request):
    numbers = request.GET['numbers']
    jnumbers = [int(i) for i in numbers.split(',')]
    jnumbers.sort()

    return JsonResponse(jnumbers, safe=False)