from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='techblog-home'),
    path('about/', views.about, name='techblog-about'),
]
