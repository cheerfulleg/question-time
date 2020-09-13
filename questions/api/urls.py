from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import QuestionViewSet, AnswerCreateAPIView, AnswerListAPIView, AnswerRUDAPIView, AnswerLikeAPIView

router = DefaultRouter()
router.register(r'questions', QuestionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('questions/<slug:slug>/answer/', AnswerCreateAPIView.as_view(), name='answer-create'),
    path('questions/<slug:slug>/answers/', AnswerListAPIView.as_view(), name='answer-list'),
    path('answers/<int:pk>/', AnswerRUDAPIView.as_view(), name='answer-detail'),
    path('answers/<int:pk>/like/', AnswerLikeAPIView.as_view(), name='answer-like'),

]


