from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Topic, Reply

def index(request):
    latest_topic_list = Topic.objects.order_by('-pub_date')[:5]
    context = { 'latest_topic_list': latest_topic_list }
    return render(request, 'topics/index.html', context)

def detail(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    return render(request, 'topics/detail.html', {'topic': topic})

def reply(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    if request.POST['reply_content']:
        new_reply = topic.reply_set.create(content=request.POST['reply_content'])
    
    
    return HttpResponseRedirect(reverse('topics:detail', args=(topic.id, )))

    
