from django.contrib import admin
from django.urls import path
from .views import (
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)

app_name = 'articles'
urlpatterns = [
    path('create/', PostCreateView.as_view(), name="create"),
    path('<slug:Slug>/', PostDetailView.as_view(), name="detail"),
    path('<slug:Slug>/update/', PostUpdateView.as_view(), name="update"),
    path('<slug:Slug>/delete/', PostDeleteView.as_view(), name="delete"),
    path('user/<str:username>', UserPostListView.as_view(), name="userpost")
]
