from django.db import models
from django.utils import timezone

#create our post object
class Post(models.Model):
	author = models.ForeignKey('auth.User') #this is a link to another model
	title = models.CharField(max_length=200) #define text with limited characters
	text = models.TextField() #define unlimited text field
	created_date = models.DateTimeField(default=timezone.now) #date and time
	published_date = models.DateTimeField(blank=True, null=True)
	
	
	def Publish(self):
		self.published_date = timezone.now()
		self.save()
		
	def __str__(self):
		return self.title #gets the post title
		

