from django.urls import path
from .views import *

urlpatterns = [

path('studentapi/',studentapi.as_view())
]