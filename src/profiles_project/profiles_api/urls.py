from django.urls import path
from . import views

urlpatterns = [
     path('sample-ApiView/',views.SampleAPIView.as_view())
]

