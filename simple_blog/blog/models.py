from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class PublishedManager(models.Manager):
	def get_queryset(self):
		return super(PublishedManager, self).get_queryset().filter(status='published')

# Create your models here.
class Post(models.Model):
	STATUS_CHOICES = (
		('draft', 'Roboczy'),
		('published', 'Opublikowany'),
		)
	title = models.CharField(
		max_length=250,
		verbose_name='Tytuł'
		)
	slug = models.SlugField(
		max_length=250,
		unique_for_date='publish'
		)
	author = models.ForeignKey(
		User, 
		related_name='blog_posts'
		)
	body = models.TextField(
		null=True,
		blank=True
		)
	publish = models.DateTimeField(
		default=timezone.now
		)
	created = models.DateTimeField(
		auto_now=True
		)
	updated = models.DateTimeField(
		auto_now=True
		)
	status = models.CharField(
		max_length=10,
		choices=STATUS_CHOICES,
		default='draft'
		)
	objects = models.Manager()
	published = PublishedManager()

	class Meta:
		ordering = ('-publish',)
		verbose_name = "Post"
		verbose_name_plural = "Posty"


	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog:post_detail', args=[self.publish.year, self.publish.strftime('%m'), self.publish.strftime('%d'), self.slug])