from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.utils.timezone import now
import datetime
import uuid
# Create your models here.

class Idea(models.Model):

	user_id 		= models.ForeignKey(User,on_delete=models.CASCADE)
	title 			= models.CharField(max_length=255,blank=True,null=True)
	sub_title 		= models.CharField(max_length=100,blank=True,null=True)
	description 	= models.TextField(blank=True, null=True)
	plan_doc 		= models.FileField(upload_to='assets/uploads/user',blank=True, null=True)
	video 			= models.FileField(upload_to='assets/uploads/user',blank=True, null=True)
	video_link      = models.TextField(blank=True, null=True)
	idea_code 		= models.CharField(max_length=100,blank=True,unique=True, default=uuid.uuid4)
	posted_time     = models.DateTimeField(default=now,blank=True)
	status          = models.CharField(blank=True,max_length=20, default=0)

	def __str__(self):
		return self.title

class IdeaImage(models.Model):
    idea_id = models.ForeignKey(Idea, on_delete=models.CASCADE)
    Image   = models.ImageField(upload_to='assets/uploads/Idea', blank=False)

    def __str__(self):
        return self.idea_id.title
