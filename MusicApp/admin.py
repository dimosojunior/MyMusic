from django.contrib import admin
from .models import *
from embed_video.admin import AdminVideoMixin

# Register your models here.
class MusicVideosAdmin(AdminVideoMixin, admin.ModelAdmin):
	pass
admin.site.register(MusicVideos, MusicVideosAdmin)


class TutorialVideosAdmin(AdminVideoMixin, admin.ModelAdmin):
	pass
admin.site.register(TutorialVideos, TutorialVideosAdmin)



admin.site.register(SendEmail)
