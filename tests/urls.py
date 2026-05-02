from django.urls import path
from .views import QuestionListAPIView, SubmitTestAPIView, TestResultListAPIView

urlpatterns = [
    path('questions/', QuestionListAPIView.as_view(), name='question-list'),
    path('submit-test/', SubmitTestAPIView.as_view(), name='submit-test'),
    path('results/', TestResultListAPIView.as_view(), name='result-list'),
]
