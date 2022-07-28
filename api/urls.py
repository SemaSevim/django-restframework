from django.urls import path
from . import views

urlpatterns = [
    #path('test/', Test.as_view()),
    path ('', views.index, name = 'index '),
]
