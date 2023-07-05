"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from queries_test import views
from rest_framework.routers import DefaultRouter
# urls.py
from django.urls import path
from google_api.views import GoogleAuthView, CalendarEventsView
router = DefaultRouter()

router.register(r'django_filters', views.SearchListView, basename='django_filters'),
urlpatterns = [
    path('calendar/events/', CalendarEventsView.as_view(), name='google-calendar-events'),
    path('calendar/GoogleAuthView/',GoogleAuthView.as_view()),
    # Add other URL patterns for other views (e.g., for create, update, delete operations)
    path('admin/', admin.site.urls),
    path('', views.Index.as_view()),
    path('api-auth/', include('rest_framework.urls'))

]
urlpatterns+=router.urls