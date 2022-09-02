from django import forms
from .models import account
from django.contrib.auth.forms import UserCreationForm

class SingupForm(UserCreationForm):
	class Meta:
		model = account
		fields = ('username',  'last_name', 'frest_name', 'email',  'address',  'body', 'image', 'date_of_birth', 'gender')
