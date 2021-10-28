from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("csv/", views.get_csv, name="get_csv"),
    path("quiz/<int:pk_quiz>/", views.quiz_view, name="quiz"),
    path("quiz/<int:pk_quiz>/<int:pk_question>/", views.question_view, name="question"),
    path("quiz/<int:pk_quiz>/<int:pk_question>/pass/<int:pk_ans>", views.question_pass, name="question_pass"),
]
