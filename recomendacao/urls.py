from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("recomendacao/", views.recomendacao, name='recomendacao'),
    path('jsonview/', views.jsonviewer, name='jsonview'),
]