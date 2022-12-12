from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.
class MusicVideos(models.Model):
	video = EmbedVideoField()
	SongName = models.CharField(max_length=1000)
	ArtistName = models.CharField(max_length=1000)
	IsFeatured = models.BooleanField(default=False, blank=True,null=True)
	IsTrending = models.BooleanField(default=False, blank=True,null=True)
	NewRelease = models.BooleanField(default=False, blank=True,null=True)
	ArtistImage = models.ImageField(default="media/media/me.jpg", upload_to="media/", blank=True,null=True)
	SongNumber = models.IntegerField(blank=True,null=True)
	Created = models.DateTimeField(auto_now_add=True)
	Type_Choices = (
			('Bongo Flavor','Bongo Flavor'),
			('Hip Hop','Hip Hop'),
			('RNB','RNB'),
		)
	SongType = models.CharField(max_length=1000, choices=Type_Choices, blank=True, null=True)
	#UploadVideo = models.VideoField()

	def __str__(self):
		return self.ArtistName + " " + "-" + self.SongName


class TutorialVideos(models.Model):
	video = EmbedVideoField()
	TutorialName = models.CharField(max_length=1000)
	ArtistName = models.CharField(max_length=1000)
	IsFeatured = models.BooleanField(default=False, blank=True,null=True)
	IsTrending = models.BooleanField(default=False, blank=True,null=True)
	NewRelease = models.BooleanField(default=False, blank=True,null=True)
	ArtistImage = models.ImageField(default="media/media/me.jpg", upload_to="media/", blank=True,null=True)
	TutorialNumber = models.IntegerField(blank=True,null=True)
	Created = models.DateTimeField(auto_now_add=True)
	Type_Choices = (
			('Python Tutorials','Python Tutorials'),
			('Django Tutorials','Django Tutorials'),
			('Html & Css Tutorials','Html & Css Tutorials'),
			('Javascript Tutorials','Javascript Tutorials'),
			('Bootstrap Tutorials','Bootstrap Tutorials'),
		)
	TutorialType = models.CharField(max_length=1000, choices=Type_Choices, blank=True, null=True)
	#UploadVideo = models.VideoField()

	def __str__(self):
		return self.ArtistName + " " + "-" + self.TutorialName




class SendEmail(models.Model):
	Email = models.EmailField(max_length=1000)

	def __str__(self):
		return self.Email

