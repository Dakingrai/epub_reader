from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('library/<id>/', views.library_list, name="library_list"),
    path('book/', views.readbook, name="readbook"),
]