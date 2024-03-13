from .models import *
from django import forms


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'subject', 'email', 'message']