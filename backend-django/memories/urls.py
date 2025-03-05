from django.urls import path

from . import views

urlpatterns = [
    path("", views.api_root),
    path("users/", views.UserList.as_view(), name="user-list"),
    path("users/<int:pk>", views.UserDetail.as_view()),
    path("memories/", views.MemoriesList.as_view(), name="memories"),
    path("memories/<int:pk>/", views.MemoryDetail.as_view()),
]
