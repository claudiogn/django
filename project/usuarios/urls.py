from django.urls import path
from usuarios.views import RegistrarUsuariosView, ContatoFormView

urlpatterns = [
    path('comprar/',RegistrarUsuariosView.as_view() , name='registrar'),
	path('contato/', ContatoFormView.as_view(), name='contato'),

]