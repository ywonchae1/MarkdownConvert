from django.urls import include, path
from .views import *

urlpatterns = [
    path('', home),
    path('submit/', result_ajax),
]