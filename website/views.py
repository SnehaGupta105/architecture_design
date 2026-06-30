from django.shortcuts import render, redirect
from .models import Contact
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    return render(request, 'home.html')


def contact(request):
    selected_plan = request.GET.get('plan', '')
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        phone = request.POST.get('phone')
        plot_size = request.POST.get('plot_size')
        plan = request.POST.get('plan')
        message = request.POST.get('message')

        Contact.objects.create(
            name=name,
            email=email,
            message=message
        )

        full_message = f"""
Name: {name}
Email: {email}
Phone: {phone}
Plot Size: {plot_size}
Selected Plan: {plan}

Subject: {subject}

Message:
{message}
"""

        send_mail(
            subject=f"New Contact Form: {subject}",
            message=full_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

        return redirect('contact')

    return render(request, 'contact.html')

def twodplans(request):
    return render(request, 'twodplans.html')

def threedelevation(request):
    return render(request, 'threedelevation.html')

def interiordesign(request):
    return render(request, 'interiordesign.html')

def consultation(request):
    return render(request, 'consultation.html')

def pricing(request):
    return render(request, 'pricing.html')


def features(request):
    return render(request, 'features.html')

def about(request):
    return render(request, 'about.html')

# Design Pages

def kitchen(request):
    return render(request, "kitchen.html")

def bathroom(request):
    return render(request, "bathroom.html")

def livingroom(request):
    return render(request, "livingroom.html")
