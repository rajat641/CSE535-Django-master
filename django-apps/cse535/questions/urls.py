from django.urls import path

from .views import QuestionsView

from . import views

app_name = "questions"

urlpatterns = [
    path("QuestionsView/", views.QuestionsView.as_view(), name="QuestionsView"),
]
