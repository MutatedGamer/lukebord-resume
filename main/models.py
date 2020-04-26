from django.db import models
from django import forms
from django.forms import ModelForm

# Create your models here.

class About(models.Model):
	header = models.CharField(max_length=200)
	body = models.TextField()
	edited_date = models.DateTimeField(auto_now = True)

class Video(models.Model):
	link = models.CharField(max_length=200)

	def __str__(self):
		return self.link

class BlogPost(models.Model):
	title = models.CharField(max_length=500)
	pub_date = models.DateTimeField('date published', auto_now = True)
	edited_date = models.DateTimeField('date last edited', auto_now = True, auto_now_add = False)
	body = models.TextField('the actual blog post')
	
	def __str__(self):
		return self.title

class Project(models.Model):
	title = models.CharField(max_length=500)
	link = models.CharField(max_length=500, default='', blank=True)
	description = models.TextField()
	image = models.ImageField(upload_to='projects/')

	def __str__(self):
		return self.title

class ProjectForm(ModelForm):
	def __init__(self, *args, **kwargs):
		super(ProjectForm, self).__init__(*args, **kwargs)
		self.fields["link"].required = False 

	class Meta:
		model = Project
		fields = ['title', 'link', 'description', 'image']

