from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.AddAlbumView.as_view(), name='add_album'),
]
