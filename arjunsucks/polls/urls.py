from django.urls import path

from . import views
# Mapping to a URL to call the view function


urlpatterns = [
    path('', views.index, name='index')
]
