from django import forms
from django.forms import ModelForm

from .models import ContactRecord

class ContactForm(ModelForm):
	class Meta:
		model = ContactRecord
		fields = ('name', 'email', 'subject', 'message')