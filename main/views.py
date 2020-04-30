from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect

from django.template import context

from django.contrib.auth import authenticate, logout

from django.contrib.auth.decorators import login_required

from .models import *

def index(request):
	context = dict()
	context['page'] = 'home'
	context['about'] = About.objects.latest('id')
	return render(request, 'main/index.html', context)

def projects(request):
	context = dict()
	context['page'] = 'projects'
	projects = Project.objects.order_by('id')
	context['projects'] = projects
	return render(request, 'main/projects.html', context)

def blog(request):
	context = dict()
	context['page'] = 'blog'
	posts = BlogPost.objects.order_by('-pub_date')
	context['posts'] = posts
	return render(request, 'main/blog.html', context)

def videos(request):
	context = dict()
	context['page'] = 'videos'
	videos = Video.objects.order_by('id')
	context['videos'] = videos
	return render(request, 'main/videos.html', context)

def resume(request):
	context = dict()
	context['page'] = 'resume'
	return render(request, 'main/resume.html', context)

def logout_user(request):
	logout(request)
	return HttpResponseRedirect('/')

@login_required
def add_video(request):
	if request.method == 'POST':
		try:
			v = Video(link=request.POST['link'])
			v.save()
			print('test')
			return HttpResponseRedirect('/videos')
		except:
			context = {'page': 'videos', 'error_message': 'Something did not work...'}
	else:
		context = dict()
	return render(request, 'main/add_video.html', context)

@login_required
def delete_video(request, video_id):
	video = get_object_or_404(Video, pk=video_id)
	video.delete()
	return HttpResponseRedirect('/videos/')

@login_required
def edit_video(request, video_id):
	if request.method == 'POST':
		video = get_object_or_404(Video, pk=video_id)
		video.link = request.POST['link']
		video.save()
		return HttpResponseRedirect('/videos')
	video = get_object_or_404(Video, pk=video_id)
	context = {'page': 'video', 'video': video}
	return render(request, 'main/edit_video.html', context)

def blog_post(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    context = {'page': 'blog', 'post': post}
    return render(request, 'main/blog_post.html', context)

@login_required
def add_blog(request):
	if request.method == 'POST':
		try:
			b = BlogPost(title=request.POST['title'], body=request.POST['body'])
			b.save()
			return HttpResponseRedirect('/blog/')
		except:
			context = {'page': 'blog', 'error_message': 'Something did not work...'}
	else:
		context = dict()
	return render(request, 'main/add_blog.html', context)


@login_required
def delete_blog(request, post_id):
	post = get_object_or_404(BlogPost, pk=post_id)
	post.delete()
	return HttpResponseRedirect('/blog/')

@login_required
def edit_blog(request, post_id):
	if request.method == 'POST':
		post = get_object_or_404(BlogPost, pk=post_id)
		post.title = request.POST['title']
		post.body = request.POST['body']
		post.save()
		return HttpResponseRedirect('/blog')
	post = get_object_or_404(BlogPost, pk=post_id)
	context = {'page': 'blog', 'post': post}
	return render(request, 'main/edit_blog.html', context)

@login_required
def add_project(request):
	if request.method == 'POST':
		form = ProjectForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/projects/')
	else:
		form = ProjectForm()
		return render(request, 'main/add_project.html', {'form': form})


@login_required
def delete_project(request, project_id):
	project = get_object_or_404(Project, pk=project_id)
	project.delete()
	return HttpResponseRedirect('/projects/')

@login_required
def edit_project(request, project_id):
	if request.method == 'POST':
		project = get_object_or_404(Project, pk=project_id)
		form = ProjectForm(request.POST, request.FILES, instance=project)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/projects')
	project = get_object_or_404(Project, pk=project_id)
	form = ProjectForm(request.POST or None, instance=project)
	context = {'page': 'project', 'form': form}
	return render(request, 'main/edit_project.html', context)

@login_required
def edit_about(request):
	if request.method == 'POST':
		about = About.objects.latest('id')
		about.header = request.POST['header']
		about.body = request.POST['body']
		about.save()
		return HttpResponseRedirect('/')
	about = About.objects.latest('id')
	context = {'about':about}
	return render(request, 'main/edit_about.html', context)
