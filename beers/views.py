from django.shortcuts import render


def first_view(request):
    return render(request, 'beers/beers.html', {'title': 'Beers'})
