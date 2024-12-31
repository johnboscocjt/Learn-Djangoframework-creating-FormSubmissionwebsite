from django.shortcuts import render, redirect
from django.http import HttpResponse
# import the tour class
# from .models import Tour
from .forms import ContactForm


# Create your views here.

# create the function to take the request
# def index(request):
#     # fetch all the our objects in the database
#     tours = Tour.objects.all()
#     # passing the context dictionary from our view to our template
#     context = {'tours':tours}
#     return render(request, 'tours/index.html', context)

# def index(request):
#     return render(request, 'django_app/index.html')


# this is a home page view function
def home_view(request):
    return render(request, 'form_app/home.html')

# define the contact_view function to handle the contact form
def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            form.send_email()  # Optionally send the email
            return redirect('contact-success')
    else:
        form = ContactForm()
    context = {'form': form}
    return render(request, 'form_app/contact.html',context)

# define the contact_success_view function to handle the success page
def contact_success_view(request):
    return render(request, 'form_app/contact_success.html')
