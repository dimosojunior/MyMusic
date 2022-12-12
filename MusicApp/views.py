from django.shortcuts import render
from django.db.models.query import QuerySet
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse, get_object_or_404

from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, FormView, DetailView, DeleteView, UpdateView, ListView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.db.models import Q
import datetime
from django.views.generic.base import TemplateView
from django.core.paginator import Paginator
#from reportlab.pdfgen import canvas
#from reportlab.lib.pagesizes import letter
#from reportlab.lib.pagesizes import landscape
#from reportlab.platypus import Image
import os
from django.conf import settings
from django.http import HttpResponse
#from django.template.loader import get_template
#from xhtml2pdf import pisa
#from django.contrib.staticfiles import finders
import calendar
from calendar import HTMLCalendar
from MusicApp.models import *
from MusicApp.forms import *
#from hitcount.views import HitCountDetailView
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from itertools import chain
import random
from django.contrib.auth.models import User, auth




from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth


# Create your views here.
def signup(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        #role = request.POST['role']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, f"Email {email} Already Taken")
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, f"Username {username} Already Taken")
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()


                #HIZI NI KWA AJILI KUTUMA EMAIL ENDAPO MTU AKIJISAJILI
                username = request.POST.get('email')
                #last_name = request.POST['last_name']
                email = request.POST.get('email')
                subject = "Welcome to MUST ARTISTS MUSICS WEBSITE"
                message = f"Ahsante  {username} kwa kujisajili na website yetu, angalia nyimbo mbalimbali za bongo zilizoimbwa na wasanii wako bomba kutoka chuo kikuu cha sayansi na teknolojia mbeya. Pata mziki mtamu umwagilie moyo "
                from_email = settings.EMAIL_HOST_USER
                recipient_list = [email]
                send_mail(subject, message, from_email, recipient_list, fail_silently=True)



                # #log user in and redirect to settings page
                # user_login = auth.authenticate(username=username, password=password)
                # auth.login(request, user_login)

                
                return redirect('signin')
        else:
            messages.info(request, 'The Two Passwords Not Matching')
            return redirect('signup')

    else:
        return render(request, 'MusicApp/signup.html')

def signin(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('signin')

    else:
        return render(request, 'MusicApp/signin.html')



def logout(request):
    auth.logout(request)
    return redirect('signin')















def home(request):
	music = MusicVideos.objects.all().order_by('-id')
	isfeatured = MusicVideos.objects.filter(IsFeatured=True).order_by('-id')[ :3]
	trending = MusicVideos.objects.filter(IsTrending=True).order_by('-id')[ :3]
	new_release = MusicVideos.objects.filter(NewRelease=True).order_by('-id')[ :3]
	context = {
		"music":music,
		"isfeatured":isfeatured,
		"trending":trending,
		"new_release":new_release,
	}

	return render(request, 'MusicApp/home.html',context)

def base(request):
	music = MusicVideos.objects.all()
	isfeatured = MusicVideos.objects.filter(IsFeatured=True).order_by('-id')[ :3]
	trending = MusicVideos.objects.filter(IsTrending=True).order_by('-id')[ :3]
	new_release = MusicVideos.objects.filter(NewRelease=True).order_by('-id')[ :3]
	context = {
		"music":music,
		"isfeatured":isfeatured,
		"trending":trending,
		"new_release":new_release,
	}

	return render(request, 'MusicApp/base.html',context)



def trending(request):
	all_trending = MusicVideos.objects.filter(IsTrending=True).order_by('-id')
	
	trending = MusicVideos.objects.filter(IsTrending=True).order_by('-id')[ :3]
	isfeatured = MusicVideos.objects.filter(IsFeatured=True).order_by('-id')[ :3]
	
	new_release = MusicVideos.objects.filter(NewRelease=True).order_by('-id')[ :3]
	
	context = {
		"all_trending":all_trending,
		
		"isfeatured":isfeatured,
		"trending":trending,
		"new_release":new_release,
	}

	return render(request, 'MusicApp/trending.html',context)



def featured(request):
	all_featured = MusicVideos.objects.filter(IsFeatured=True).order_by('-id')
	
	trending = MusicVideos.objects.filter(IsTrending=True).order_by('-id')[ :3]
	isfeatured = MusicVideos.objects.filter(IsFeatured=True).order_by('-id')[ :3]
	
	new_release = MusicVideos.objects.filter(NewRelease=True).order_by('-id')[ :3]
	
	context = {
		"all_featured":all_featured,
		
		"isfeatured":isfeatured,
		"trending":trending,
		"new_release":new_release,
	}

	return render(request, 'MusicApp/featured.html',context)



def new_release(request):
	all_new_release = MusicVideos.objects.filter(NewRelease=True).order_by('-id')
	
	trending = MusicVideos.objects.filter(IsTrending=True).order_by('-id')[ :3]
	isfeatured = MusicVideos.objects.filter(IsFeatured=True).order_by('-id')[ :3]
	
	new_release = MusicVideos.objects.filter(NewRelease=True).order_by('-id')[ :3]
	
	context = {
		"all_new_release":all_new_release,
		
		"isfeatured":isfeatured,
		"trending":trending,
		"new_release":new_release,
	}

	return render(request, 'MusicApp/new_release.html',context)






def bongo_flavor(request):
	bongo_flavor = MusicVideos.objects.filter(SongType='Bongo Flavor').order_by('-id')
	
	trending = MusicVideos.objects.filter(IsTrending=True).order_by('-id')[ :3]
	isfeatured = MusicVideos.objects.filter(IsFeatured=True).order_by('-id')[ :3]
	
	new_release = MusicVideos.objects.filter(NewRelease=True).order_by('-id')[ :3]
	
	context = {
		"bongo_flavor":bongo_flavor,
		
		"isfeatured":isfeatured,
		"trending":trending,
		"new_release":new_release,
	}

	return render(request, 'MusicApp/bongo_flavor.html',context)


def rnb(request):
	rnb = MusicVideos.objects.filter(SongType='RNB').order_by('-id')
	
	trending = MusicVideos.objects.filter(IsTrending=True).order_by('-id')[ :3]
	isfeatured = MusicVideos.objects.filter(IsFeatured=True).order_by('-id')[ :3]
	
	new_release = MusicVideos.objects.filter(NewRelease=True).order_by('-id')[ :3]
	
	context = {
		"rnb":rnb,
		
		"isfeatured":isfeatured,
		"trending":trending,
		"new_release":new_release,
	}

	return render(request, 'MusicApp/rnb.html',context)


def hiphop(request):
	hiphop = MusicVideos.objects.filter(SongType='Hip Hop').order_by('-id')
	
	trending = MusicVideos.objects.filter(IsTrending=True).order_by('-id')[ :3]
	isfeatured = MusicVideos.objects.filter(IsFeatured=True).order_by('-id')[ :3]
	
	new_release = MusicVideos.objects.filter(NewRelease=True).order_by('-id')[ :3]
	
	context = {
		"hiphop":hiphop,
		
		"isfeatured":isfeatured,
		"trending":trending,
		"new_release":new_release,
	}

	return render(request, 'MusicApp/hiphop.html',context)



def search_music(request):
	trending = MusicVideos.objects.filter(IsTrending=True).order_by('-id')[ :3]
	isfeatured = MusicVideos.objects.filter(IsFeatured=True).order_by('-id')[ :3]

	new_release = MusicVideos.objects.filter(NewRelease=True).order_by('-id')[ :3]

	query=None
	results=[]

	if request.method == "GET":
	    query=request.GET.get("search")
	    mysearch=Q(SongName__icontains=query)|Q(ArtistName__icontains=query)
	    results=MusicVideos.objects.filter(mysearch)
	context={
	    
	    "query":query,
	    "results":results,

	    "isfeatured":isfeatured,
		"trending":trending,
		"new_release":new_release,
	}
	return render(request, 'MusicApp/search_music.html',context)


def search_music_autocomplete(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(SongName__icontains=query_original)#|Q(ArtistName__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    music = MusicVideos.objects.filter(search)
    mylist= []
    mylist += [x.SongName for x in music]
    return JsonResponse(mylist, safe=False)










def view_music(request,id):
	view_music = MusicVideos.objects.get(id=id)
	
	
	trending = MusicVideos.objects.filter(IsTrending=True).order_by('-id')[ :3]
	isfeatured = MusicVideos.objects.filter(IsFeatured=True).order_by('-id')[ :3]
	
	new_release = MusicVideos.objects.filter(NewRelease=True).order_by('-id')[ :3]
	
	context = {
		"view_music":view_music,
		
		"isfeatured":isfeatured,
		"trending":trending,
		"new_release":new_release,
	}

	return render(request, 'MusicApp/view_music.html',context)




def upload_music(request):
	
	
	
	trending = MusicVideos.objects.filter(IsTrending=True).order_by('-id')[ :3]
	isfeatured = MusicVideos.objects.filter(IsFeatured=True).order_by('-id')[ :3]
	
	new_release = MusicVideos.objects.filter(NewRelease=True).order_by('-id')[ :3]

	form = UploadMusicForm()
	if request.method == "POST":
		form = UploadMusicForm(request.POST, files=request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, "Music Uploaded Successful!!!")
			return redirect('home')
		messages.info(request, "Failde to Upload this song")
		return redirect('upload_music')

	
	context = {
		"form":form,
		
		"isfeatured":isfeatured,
		"trending":trending,
		"new_release":new_release,
	}

	return render(request, 'MusicApp/upload_music.html',context)













#-------------------------------TUTORIALS----------------------------------

def tutorials_home(request):
	tutorial = TutorialVideos.objects.all().order_by('?')
	isfeatured = TutorialVideos.objects.filter(IsFeatured=True).order_by('-id')[ :3]
	trending = TutorialVideos.objects.filter(IsTrending=True).order_by('-id')[ :3]
	new_release = TutorialVideos.objects.filter(NewRelease=True).order_by('-id')[ :3]
	context = {
		"tutorial":tutorial,
		"isfeatured":isfeatured,
		"trending":trending,
		"new_release":new_release,
	}

	return render(request, 'Tutorials/tutorials_home.html',context)


def tutorials_base(request):
	music = TutorialVideos.objects.all()
	isfeatured = TutorialVideos.objects.filter(IsFeatured=True).order_by('-id')[ :1]
	trending = TutorialVideos.objects.filter(IsTrending=True).order_by('-id')[ :3]
	new_release = TutorialVideos.objects.filter(NewRelease=True).order_by('-id')[ :3]
	context = {
		"music":music,
		"isfeatured":isfeatured,
		"trending":trending,
		"new_release":new_release,
	}

	return render(request, 'Tutorials/tutorials_base.html',context)


def view_tutorial(request,id):
	view_tutorial = TutorialVideos.objects.get(id=id)
	
	
	trending = TutorialVideos.objects.filter(IsTrending=True).order_by('-id')[ :3]
	isfeatured = TutorialVideos.objects.filter(IsFeatured=True).order_by('-id')[ :3]
	
	new_release = TutorialVideos.objects.filter(NewRelease=True).order_by('-id')[ :3]
	
	context = {
		"view_tutorial":view_tutorial,
		
		"isfeatured":isfeatured,
		"trending":trending,
		"new_release":new_release,
	}

	return render(request, 'Tutorials/view_tutorial.html',context)




def python(request):
	python = TutorialVideos.objects.filter(TutorialType='Python Tutorials').order_by('?')
	
	trending = TutorialVideos.objects.filter(IsTrending=True).order_by('-id')[ :3]
	isfeatured = TutorialVideos.objects.filter(IsFeatured=True).order_by('-id')[ :3]
	
	new_release = TutorialVideos.objects.filter(NewRelease=True).order_by('-id')[ :3]
	
	context = {
		"python":python,
		
		"isfeatured":isfeatured,
		"trending":trending,
		"new_release":new_release,
	}

	return render(request, 'Tutorials/python.html',context)



def django(request):
	django = TutorialVideos.objects.filter(TutorialType='Django Tutorials').order_by('?')
	
	trending = TutorialVideos.objects.filter(IsTrending=True).order_by('-id')[ :3]
	isfeatured = TutorialVideos.objects.filter(IsFeatured=True).order_by('-id')[ :3]
	
	new_release = TutorialVideos.objects.filter(NewRelease=True).order_by('-id')[ :3]
	
	context = {
		"django":django,
		
		"isfeatured":isfeatured,
		"trending":trending,
		"new_release":new_release,
	}

	return render(request, 'Tutorials/django.html',context)



def html_css(request):
	html_css = TutorialVideos.objects.filter(TutorialType='Html & Css Tutorials').order_by('?')
	
	trending = TutorialVideos.objects.filter(IsTrending=True).order_by('-id')[ :3]
	isfeatured = TutorialVideos.objects.filter(IsFeatured=True).order_by('-id')[ :3]
	
	new_release = TutorialVideos.objects.filter(NewRelease=True).order_by('-id')[ :3]
	
	context = {
		"html_css":html_css,
		
		"isfeatured":isfeatured,
		"trending":trending,
		"new_release":new_release,
	}

	return render(request, 'Tutorials/html_css.html',context)


def javascript(request):
	javascript = TutorialVideos.objects.filter(TutorialType='Javascript Tutorials').order_by('?')
	
	trending = TutorialVideos.objects.filter(IsTrending=True).order_by('-id')[ :3]
	isfeatured = TutorialVideos.objects.filter(IsFeatured=True).order_by('-id')[ :3]
	
	new_release = TutorialVideos.objects.filter(NewRelease=True).order_by('-id')[ :3]
	
	context = {
		"javascript":javascript,
		
		"isfeatured":isfeatured,
		"trending":trending,
		"new_release":new_release,
	}

	return render(request, 'Tutorials/javascript.html',context)



def bootstrap(request):
	bootstrap = TutorialVideos.objects.filter(TutorialType='Bootstrap Tutorials').order_by('?')
	
	trending = TutorialVideos.objects.filter(IsTrending=True).order_by('-id')[ :3]
	isfeatured = TutorialVideos.objects.filter(IsFeatured=True).order_by('-id')[ :3]
	
	new_release = TutorialVideos.objects.filter(NewRelease=True).order_by('-id')[ :3]
	
	context = {
		"bootstrap":bootstrap,
		
		"isfeatured":isfeatured,
		"trending":trending,
		"new_release":new_release,
	}

	return render(request, 'Tutorials/bootstrap.html',context)






def search_tutorial(request):
	trending = TutorialVideos.objects.filter(IsTrending=True).order_by('-id')[ :3]
	isfeatured = TutorialVideos.objects.filter(IsFeatured=True).order_by('-id')[ :3]

	new_release = TutorialVideos.objects.filter(NewRelease=True).order_by('-id')[ :3]

	query=None
	results=[]

	if request.method == "GET":
	    query=request.GET.get("search")
	    mysearch=Q(TutorialName__icontains=query)|Q(ArtistName__icontains=query)
	    results=TutorialVideos.objects.filter(mysearch)
	context={
	    
	    "query":query,
	    "results":results,

	    "isfeatured":isfeatured,
		"trending":trending,
		"new_release":new_release,
	}
	return render(request, 'Tutorials/search_tutorial.html',context)


def search_tutorial_autocomplete(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(TutorialName__icontains=query_original)#|Q(ArtistName__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    tutorial = TutorialVideos.objects.filter(search)
    mylist= []
    mylist += [x.TutorialName for x in tutorial]
    return JsonResponse(mylist, safe=False)








def send_email(request):
	

	form = SendEmailForm()
	if request.method == "POST":
		form = SendEmailForm(request.POST, files=request.FILES)
		if form.is_valid():
			form.save()


			#HIZI NI KWA AJILI KUTUMA EMAIL ENDAPO MTU AKIJISAJILI
			username = request.user
			#last_name = request.POST['last_name']
			email = request.POST.get('Email')
			subject = "Welcome to MUST ARTISTS MUSICS WEBSITE"
			message = f"Ahsante  {username} kwa kujisajili na website yetu, angalia nyimbo mbalimbali za bongo zilizoimbwa na wasanii wako bomba kutoka chuo kikuu cha sayansi na teknolojia mbeya. Pata mziki mtamu umwagilie moyo "
			from_email = settings.EMAIL_HOST_USER
			recipient_list = [email]
			send_mail(subject, message, from_email, recipient_list, fail_silently=True)
			#messages.success(request, "Email Sent Successful!!!")
			return HttpResponse("Email Sent Successful!!!")
		

	
	

	