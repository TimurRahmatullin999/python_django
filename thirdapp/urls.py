from django.urls import path
from thirdapp.views import luck, allright, lazy

urlpatterns = [
    path('luck/', luck),
    path('allright/', allright),
    path('lazy', lazy)
]
