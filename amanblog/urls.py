"""amanblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

"""
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from articles import views as articles_views
from django.contrib.auth import views as auth_views
from accounts import views as account_views
from .views import PostListView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about, name="blog-about"),
    path('articles/', include('articles.urls')),
    path('', PostListView.as_view(), name="blog-home"),
    path('accounts/', include('accounts.urls'), name='blog-accounts'),
    path('signup/', account_views.signup_view, name="signup"),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('profile/', account_views.profile_view, name="profile")

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# django knows to put the media files in this path only
