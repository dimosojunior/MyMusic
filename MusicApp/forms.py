from MusicApp.models import *
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate


class UploadMusicForm(forms.ModelForm):

	class Meta:
		model = MusicVideos
		fields = '__all__'

class SendEmailForm(forms.ModelForm):

	class Meta:
		model = SendEmail
		fields = '__all__'