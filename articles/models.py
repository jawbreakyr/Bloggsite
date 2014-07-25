from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone

from easy_thumbnails.fields import ThumbnailerImageField

# Create your models here.
class Category(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(unique=True)

	class Meta:
		verbose_name_plural = 'Categories'

	def __unicode__(self):
		return self.title

class Article(models.Model):
	DRAFT = 1
	PUBLISHED = 2 
	STATUS_CHOICE = (
		(DRAFT, 'draft'),
		(PUBLISHED, 'published'),
		)

	title = models.CharField(max_length=200)
	slug = models.SlugField(unique=True)
	body = models.TextField()
	status = models.IntegerField(choices=STATUS_CHOICE, default=DRAFT)
	published_date = models.DateTimeField(default=datetime.now)
	category = models.ForeignKey(Category)
	author = models.ForeignKey(User)
	image = ThumbnailerImageField(upload_to='image', blank=True)

	def was_published_recently(self):
		return self.published_date >= timezone.now() - datetime.timedelta(days=1)
		was_published_recently.admin_order_field = "published_date"
		was_published_recently.boolean = True
		was_published_recently.short_description = "Published recently?"

	# class Meta:
	# 	ordering = ('published_date',)

	def __unicode__(self):
		return self.title