from django.shortcuts import render



meetups = [
        {
            'title': 'The first meetups',
            'description': 'This is the first meetup',
            'slug': 'a-first-meetup'
        },
        {
            'title': 'The first meetups',
            'description': 'This is the first meetup',
            'slug': 'a-first-meetup'
        }
    ]

def index(request):

    return render(request, 'meetups/index.html', {
        'meetups': meetups
    })


def index_detail(request, my_slug):
    for meetup in meetups:
        if meetup['slug'] == my_slug:
            description = meetup['description']
            return render(request, 'meetups/meetup-details.html', {
                "meetup_description": description
            })
