from django.urls import path

from .views import UserDisplayAPIView


urlpatterns = [
    path('user/', UserDisplayAPIView.as_view(), name='current-user')
]