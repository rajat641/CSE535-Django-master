from django.urls import path

from .views import PreferencesView

from . import views

app_name = "preferences"

urlpatterns = [
    path('preferences/', PreferencesView.as_view()),
    path("pref_save/", views.pref_save.as_view(), name="pref_save"),
]
