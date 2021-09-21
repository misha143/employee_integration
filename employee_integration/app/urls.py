from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("csv/", views.get_csv, name="get_csv"),
    path("quiz/<int:pk_quiz>/", views.quiz_view, name="quiz"),
    path("quiz/<int:pk_quiz>/pass/<int:pk_ans>", views.quiz_pass, name="quiz_pass"),
]
