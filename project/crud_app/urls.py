from django.urls import path
from .views import *
urlpatterns = [
    path('create/',Create_Event.as_view(),name='create_url'),
    path('show/',Show_Event.as_view(),name='show_url'),
    path('update/<int:pk>/',Update_Event.as_view(),name='update_url'),
    path('delete/<int:pk>/',Delete_Event.as_view(),name='delete_url')
]