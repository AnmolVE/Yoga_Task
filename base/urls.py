from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('achievement/', achievement, name="achievement"),
    path('helpline/', helpline, name="helpline"),
    path('donation/', donation, name="donation"),
]