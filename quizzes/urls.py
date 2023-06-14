from django.urls import path
from quizzes import views

urlpatterns = [
    path("", views.QuizView.as_view(), name="quiz"),
    path("suggest/", views.QuizSuggestView.as_view(), name="quiz_suggest"),
    path("<int:quiz_id>/", views.QuizReportView.as_view(), name="quiz_report"),
]
