"""ZatLanSone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from zatlansone import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('stories/', views.story_view, name='story'),
    path('stories/<int:story_id>/', views.episode_view, name='episode'),
    path('stories/<int:episode_id>/content', views.content_view, name='content'),
    path('stories/search_stories/', views.search_stories, name='search-stories'),
    path('maintenance/', views.maintenance, name="maintenance"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
