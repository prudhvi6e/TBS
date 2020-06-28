from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def home(request):
	return render(request, 'home.html', {})

def artist(request):
	return render(request, 'artist.html', {})

def blog(request):
	return render(request, 'blog.html', {})

def category(request):
	return render(request, 'category.html', {})

def playlist(request):
	return render(request, 'playlist.html', {})

def contact(request):
	if request.method == "POST":
		#do stuff
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']
		#send mail
		send_mail(
			message_name, #subject
			message, #message
			message_email, #from email
			['prudhvi6e@gmail.com'], #to email
			)
		return render(request, 'contact.html', {'message-name': message-name})

	else:
		return render(request, 'contact.html', {})
