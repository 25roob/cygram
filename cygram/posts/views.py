"""Posts views"""

# Django
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone


posts = [
    {
        'name':'Mont Blac',
        'user': 'Yésica Cortéz',
        'timestamp': timezone.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/237/200/200'
    },
    {
        'name': 'Khe.',
        'user': 'Pink Woman',
        'timestamp': timezone.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/84/200/200'
    },
    {
        'name': 'Nautural web.',
        'user': 'Pancho Villa',
        'timestamp': timezone.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/784/200/200'
    },
]


def list_posts(request):
    """List existing posts."""
    content = []
    for post in posts:
        content.append("""
            <p><strong>{name}</strong></p>
            <p><small>{user} - <i>{timestamp}</i></small></p>
            <figure><img src="{picture}"></figure>
        """.format(**post))
    return HttpResponse('<br>'.join(content))