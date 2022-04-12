from django.db import models


class Post(models.Model):
	title = models.CharField(max_length=300)
	date = models.DateTimeField()
	text = models.CharField(max_length=300)
	event_image = models.ImageField(upload_to='event_images/')
