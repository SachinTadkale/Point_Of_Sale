from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.contrib import messages
from .forms import ContactForm

# Create your views here.

def about(request):
  return render(request,'core/about.html')

def contact(request):
  return render(request,'core/contact.html')

def dashboard(request):
  return render(request,'core/dashboard.html')

def home(request):
  return render(request,'core/home.html')

def landing(request):
  return render(request,'landing.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject = f'Contact Form Submission from {name}'
            body = f'Name: {name}\nEmail: {email}\n\nMessage:\n{message}'
            email_message = EmailMessage(
                subject,
                body,
                email,  # from email (user's input)
                ['sachintadkale1221@gmail.com'],
                reply_to=[email],
            )
            email_message.send(fail_silently=False)
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('core:contact')  # Redirect to the contact page
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
    return render(request, 'landing.html', {'contact_form': form})