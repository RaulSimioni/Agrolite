from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("login/", views.login, name='login_user'),
    path("register/", views.register, name='register'),
    path("recomendacao/", views.recomendacao, name='recomendacao'),
    path("logout_user/", views.logout_user, name='logout_user'),
    path("historico/", views.Historico, name='historico'),
]