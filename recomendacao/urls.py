from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("registrar/", views.registrar, name='registrar'),
    path("recomendacao/", views.recomendacao, name='recomendacao'),
    path("login/", views.login, name='login'),
    path("logout", views.logout, name='logout'),
]