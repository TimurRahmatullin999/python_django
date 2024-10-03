from django.urls import path
from firstapp.views import index, bithday, cat

urlpatterns = [
    path('', index),
    path('bithday/', bithday),
    path('cat/', cat)
]
