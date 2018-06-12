from django import forms
from django.contrib.auth.models import User

class RegistrarUsuarioForm(forms.Form):
	CHOICES=[('Caixa','select 1'),('Bradesco','select 2'),('MercadoPago','select 3')]
	pagamento = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
	name=forms.CharField(required=True)
	email=forms.EmailField(required=True)
	wallet=forms.CharField(required=True)
	termos = forms.BooleanField(required=True)
	valor = forms.CharField(required=True)
	comprovante = forms.FileField(required=False)
	message = forms.CharField(required=True)
	

	def is_valid(self):
		valid = True
		if not super().is_valid():
			print ('error no super')
			self.adiciona_erro('Verifique os dados informados')
			valid=False
		return valid

	def adiciona_erro(self,message):
		erros=self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
		erros.append(message)

class ContatoForm(forms.Form):
	name=forms.CharField(required=True)
	email=forms.EmailField(required=True)
	subject=forms.CharField(required=True)
	message = forms.CharField(required=True)


	def is_valid(self):
		valid = True
		if not super().is_valid():
			print ('error no super')
			self.adiciona_erro('Verifique os dados informados')
			valid=False
		return valid

	def adiciona_erro(self,message):
		erros=self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
		erros.append(message)