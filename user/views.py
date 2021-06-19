from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .forms import UserRegisterForm
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from ticketit import settings

#################### index #######################################
def index(request):
	return render(request, 'user/home.html', {'title':'home'})

########### register here #####################################

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			email = form.cleaned_data.get('email')
			try:
				user = User.objects.get(email=email)
				if user is not None:
					messages.info(request, f'email already linked to an account')
					form = AuthenticationForm()
					return render(request, 'user/login.html', {'form':form, 'title':'log in'})
			except:

			######################### mail system ####################################
				htmly = get_template('user/Email.html')
				d = { 'username': username, 'message': 'we have received your details and will process soon.' }
				subject, from_email, to = 'welcome',settings.EMAIL_HOST_USER, email
				html_content = htmly.render(d)
				msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
				msg.attach_alternative(html_content, "text/html")
				msg.send()
				##################################################################
				messages.success(request, f'Your account has been created ! You are now able to log in')
				return redirect('login')
	else:
	    form = UserRegisterForm()
	return render(request, 'user/register.html', {'form': form, 'title':'reqister here'})
 
################ login forms###################################################
def Login(request):
	if request.method == 'POST':

		# AuthenticationForm_can_also_be_used__

		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username = username, password = password)
		if user is not None:
			form = login(request, user)
			messages.success(request, f' wecome {username} !!')
			return redirect('home')
		else:
			messages.info(request, f'Incorrect details(Username and Password)')
	form = AuthenticationForm()
	return render(request, 'user/login.html', {'form':form, 'title':'log in'})

@login_required
def update_profile(request):
	if request.method == 'POST':
		user = User.objects.get(email=request.user.email)
		if request.POST.get('first_name') != '':
			user.first_name = request.POST.get('first_name')
		if request.POST.get('last_name') != '':
			user.last_name = request.POST.get('last_name')
		if request.POST.get('email') != '':
			user.email = request.POST.get('email')
		if request.POST.get('username') != '':
			user.username = request.POST.get('username')
		
		user.save()
		return redirect('home')
	return redirect('home')


@login_required
def update_password(request):
	if request.method == 'POST':
		email = request.user.email
		currentPassword = request.POST.get('password1')
		user = User.objects.get(email=email)
		if request.POST.get('password2') == request.POST.get('password3'):
			user.set_password(request.POST.get('password2'))
			user.save()
			print(user.password)
		return redirect('home')
	return redirect('home')