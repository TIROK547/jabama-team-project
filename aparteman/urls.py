from django.urls import path
from .views import aparteman
urlpatterns = [
    path("aparteman/view-royayee",aparteman(0)),
    path("aparteman/sargarmi",aparteman(1)),
]