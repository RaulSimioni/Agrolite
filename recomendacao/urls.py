from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("login/", views.login, name='login_user'),
    path("register/", views.register, name='register'),
    path("recomendacao/", views.recomendacao, name='recomendacao'),
    path("logout_user/", views.logout_user, name='logout_user'),
    path("historico/", views.Historico_view, name='historico'),
    path('deletar_historico/<int:historico_id>/', views.deletar_historico, name='deletar_historico'),
    path('Menu_avancado/', views.Menu_avancado, name='Menu_avancado'),
]