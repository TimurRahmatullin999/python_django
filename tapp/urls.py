from django.urls import path
from tapp.views import gh, drive, evening

urlpatterns = [
    path('gh/', gh),
    path('drive/', drive),
    path('evening/', evening)
]