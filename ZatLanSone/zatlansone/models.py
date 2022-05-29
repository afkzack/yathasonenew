from django.db import models
from django.utils import timezone

# Create your models here.

class Episode(models.Model):

	name = models.CharField(max_length=100, null=True, blank=True)
	ep_num = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=1)

	def __str__(self):
		return self.name + " | Episode - " + str(self.ep_num)

class Content(models.Model):
	image = models.ImageField(blank=True, null=True)
	description = models.TextField(null=True, blank=True)
	episode = models.ForeignKey(Episode, default=None, on_delete=models.CASCADE)

	def __str__(self):
		return self.episode.name


class Story(models.Model):
	name = models.CharField(max_length=300)
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(auto_now_add=True,blank=True, null=True)
	image = models.ImageField(blank=True, null=True)
	eps = models.ManyToManyField(Episode, blank=True)
	cover = models.ImageField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.name
