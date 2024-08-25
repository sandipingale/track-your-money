from django.urls import path
from . import views
urlpatterns = [
    path("", views.ShareProcess.as_view(), name="shares-add" ),
    path("list", views.ShareListView.as_view(), name="shares-list" ),
]