from django.shortcuts import render
from .forms import ContactForm, VolunteerForm
from .helpers import send_emails


# Home page
def index(request):
    context = {'segment': 'index'}
    return render(request, 'core/index.html', context)


# Contact page
def contact(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'New Message from Seeds of Leadership Website'
            body = f"""
            Name: {form.cleaned_data['name']}
            Email: {form.cleaned_data['email']}
            Message: {form.cleaned_data['message']}
            """

            send_emails(request, subject, body)

    context = {'segment': 'contact', 'page': 'contact us', 'form': form}
    return render(request, 'core/contact.html', context)


# Contact page
def about(request):
    context = {'segment': 'about', 'page': 'about us'}
    return render(request, 'core/about.html', context)


# Gallery page
def gallery(request):
    context = {'segment': 'gallery', 'page': 'gallery'}
    return render(request, 'core/gallery.html', context)


# Volunteer page
def volunteer(request):
    form = VolunteerForm()

    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        if form.is_valid():
            subject = "New Volunteer Request from Seeds of Leadership Website"
            body = f"""
            Name: {form.cleaned_data['name']}
            Email: {form.cleaned_data['email']}
            Phone: {form.cleaned_data['phone']}
            Address: {form.cleaned_data['address']}
            Reason: {form.cleaned_data['reason']}
            """

            send_emails(request, subject, body)

    context = {'segment': 'volunteer', 'page': 'Volunteer', 'form': form}
    return render(request, 'core/volunteer.html', context)


# Donate page
def donate(request):
    context = {'segment': 'donate', 'page': 'Donate'}
    return render(request, 'core/donate.html', context)