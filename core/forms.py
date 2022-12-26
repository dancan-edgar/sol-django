from django import forms
from django.forms import ModelForm

from .models import Contact, Volunteer


# Contact form
class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={'placeholder': 'Enter your name',
                       'class': 'form-control form-control-lg rounded-0'}),
            'email': forms.EmailInput(
                attrs={'placeholder': 'Enter your email',
                       'class': 'form-control form-control-lg rounded-0'}),
            'message': forms.Textarea(
                attrs={'placeholder': 'Enter Message',
                       'class': 'form-control form-control-lg rounded-0',
                       'rows': 5}),
        }


# Volunteer form
class VolunteerForm(ModelForm):
    class Meta:
        model = Volunteer
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={'placeholder': 'Enter Name',
                       'class': 'form-control form-control-lg rounded-0'}),
            'email': forms.EmailInput(
                attrs={'placeholder': 'Enter Email',
                       'class': 'form-control form-control-lg rounded-0'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Enter Phone Number',
                                            'class': 'form-control form-control-lg rounded-0'}),
            'address':  forms.TextInput(
                attrs={'placeholder': 'Enter Address',
                       'class': 'form-control form-control-lg rounded-0'}),
            'reason': forms.Textarea(
                attrs={'placeholder': 'Enter Reason',
                       'class': 'form-control form-control-lg rounded-0',
                       'rows': 5}),
        }
