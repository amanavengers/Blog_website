from django.contrib import admin
from django.urls import path
from .views import (
    Post_Article_ListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

app_name = 'articles'
urlpatterns = [
    path('', Post_Article_ListView.as_view(), name="list"),
    path('create/', PostCreateView.as_view(), name="create"),
    path('<slug:Slug>/', PostDetailView.as_view(), name="detail"),
    path('<slug:Slug>/update/', PostUpdateView.as_view(), name="update"),
    path('<slug:Slug>/delete/', PostDeleteView.as_view(), name="delete")
]
