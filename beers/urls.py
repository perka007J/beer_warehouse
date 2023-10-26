from django.urls import path
import beers.views as vs


urlpatterns = [
    path('', vs.first_view, name='first_view')
]
