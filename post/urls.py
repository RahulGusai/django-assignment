from django.urls import path

from . import views

app_name = 'post'
urlpatterns = [
    path('api', views.postAPI.as_view(), name='postAPI'),
]
