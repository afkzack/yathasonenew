from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import *

def index_view(request):
	return render(request, 'index.html')

def home_view(request):
	return render(request, 'home.html')

def maintenance(request):
	return render(request, 'maintenance.html')

def story_view(request):
	story = Story.objects.all()
	context = {'story':story}
	return render(request, 'story.html', context)

def episode_view(request, story_id):
	story = get_object_or_404(Story, pk=story_id)
	episode = Episode.objects.filter(story=story)
	context = {
	'story':story,
	'episode':episode
	}
	return render(request, 'episode.html', context)

def content_view(request, episode_id):
	episode = get_object_or_404(Episode, pk=episode_id)
	content = Content.objects.filter(episode=episode)
	context = {
	'episode':episode,
	'content':content
	}
	return render(request, 'content.html', context)

def search_stories(request):
	if request.method == "POST":
		searched = request.POST['searched']
		stories = Story.objects.filter(name__contains=searched)
		return render(request, 'search_stories.html', {'searched':searched, 'stories':stories})
	else:
		return render(request, 'search_stories.html', {})