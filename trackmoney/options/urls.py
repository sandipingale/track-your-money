from django.urls import path, include
from . import views

urlpatterns = [
    path("test/", views.test_options, name="test_options"),
    path("test-options/", views.Options.as_view()),
]
