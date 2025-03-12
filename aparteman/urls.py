from django.urls import path
from .views import aparteman
from functools import partial

urlpatterns = [
    path("aparteman/view-royayee", partial(aparteman, 0)),
    path("aparteman/sargarmi", partial(aparteman, 1)),
]