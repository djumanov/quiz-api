from django.urls import path
from .views import QuizListView, QuestionListView, CheckView

urlpatterns = [
    path('quiz/', QuizListView.as_view()),
    path('quiz/<int:pk>/', QuestionListView.as_view()),
    path('quiz/check/<int:pk>/', CheckView.as_view()),
]