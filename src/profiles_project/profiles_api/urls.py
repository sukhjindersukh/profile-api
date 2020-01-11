from django.urls import path, include

#To use viewSet we need this import
from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter()

# Here we need to register our all viewSet with router
router.register(r'sample-ViewSet', views.SampleViewSet, basename='sample-ViewSet')
router.register('profile',views.UserProfileViewSet)


urlpatterns = [
     path('sample-ApiView/',views.SampleAPIView.as_view()),
]

urlpatterns = urlpatterns + router.urls

