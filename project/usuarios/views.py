from django.shortcuts import render, redirect
from django.views.generic.base import View
from usuarios.forms import RegistrarUsuarioForm, ContatoForm
from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives
from bitcoin.models import Perfil
from django.conf import settings
from django.template.loader import render_to_string
# tirar algumas coisas do template, ver se consigo mostrar o arquivo anexado

# Create your views here.

class RegistrarUsuariosView(View):
	def get(self, request):
		return render(request, 'registrar.html')


	def post(self, request):
		form= RegistrarUsuarioForm(request.POST, request.FILES)
		if form.is_valid():
			dados_form=form.data
			print(dados_form)
			subject='Nova compra'
			from_email=settings.EMAIL_HOST_USER
			to_email = [dados_form['email']]
			# body = (' Nome: {} \n Email: {} \n Carteira Bitcoin: {} \n Forma de Pagamento: {} \n'
			#  		'Valor depositado: {} \n Mensagem: {} \n'.format(dados_form['name'], dados_form['email'], dados_form['wallet'], dados_form['pagamento'], dados_form['valor'], dados_form['message']))
			html_content = render_to_string('bitcoin_compra.html', {'dados':dados_form})
			email=EmailMultiAlternatives(
				subject,
				html_content,
				from_email,
				to_email
				)
			if request.FILES:
				comprovante = request.FILES['comprovante']
				email.attach(comprovante.name, comprovante.read(), comprovante.content_type)
			email.attach_alternative(html_content, "text/html")
			email.send()
			# print(body)
			return redirect('index')
		return render(request, 'registrar.html', {'form':form})

class ContatoFormView(View):
	def get(self,request):
		return render (request, 'contato.html')
	def post(self, request):
		form = ContatoForm(request.POST)
		if form.is_valid():
			dados_form=form.data
			subject='Mensagem do Cliente'
			name=dados_form['name']
			from_email=dados_form['email']
			message=dados_form['message']
			to_email = [settings.EMAIL_HOST_USER]
			# body = ' De: {} \n Assunto: {} \n Mensagem: {} \n'.format(from_email, subject, message)
			html_content = render_to_string('bitcoin_contato.html', {'dados':dados_form})
			email = EmailMultiAlternatives(
				subject,
				html_content,
				from_email,
				to_email
				)
			email.attach_alternative(html_content, "text/html")
			email.send()
			# print (body)
			return redirect('index')

		return render(request, 'contato.html', {'form':form})







