#Python
import pdb
import json

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


def hi2(request):
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted succesfully.'
    }
    # pdb.set_trace()
    return HttpResponse(json.dumps(data, indent=4), content_type="application/json")


def hi3(request, name, age):
    if age < 12:
        message = f'Sorry {name}, you are not allowed here.'
    else:
        message = f'Hello {name}! Welcome to Cygram.'
    return HttpResponse(message)