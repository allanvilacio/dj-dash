from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_dash, name='home-dash'),
    path('graph', views.graph_view)
]
