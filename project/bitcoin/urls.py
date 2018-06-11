from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('perfis/<int:perfil_id>/', views.exibir, name='exibir'),
    path('perfis/<int:perfil_id>/convidar', views.convidar, name='convidar'),
    path('termos-e-condicoes', views.termos_e_condicoes, name='termos_e_condicoes'),
    path('politica-de-privacidade', views.politica_de_privacidade, name='politica_de_privacidade'),
    path('politica-de-reembolso', views.politica_de_reembolso, name='politica_de_reembolso'),
    path('convite/<int:convite_id>/aceitar', views.aceitar, name='aceitar'),
]