from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.AddMusicianView.as_view(), name='add_musician'),
    path('update/<int:id>/', views.EditMusicianView.as_view(), name='update_musician'),
    path('delete/<int:id>/', views.DeleteMusicianView.as_view(), name='delete_musician'),
]
