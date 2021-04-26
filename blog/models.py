from django.db import models

# Create your models here.

class Blog_project(models.Model):
	title = models.CharField(max_length=100)
	date = models.DateTimeField(auto_now=False, auto_now_add=False)
	description = models.TextField()
	image = models.ImageField(upload_to='blog/images/')
	url = models.URLField(blank=True)

	def __str__(self):
		return self.title + "  |  " + str(self.date)
