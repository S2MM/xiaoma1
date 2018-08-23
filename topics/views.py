from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.urls import reverse
from django.views import generic

from .models import Topic, Reply

class IndexView(generic.ListView):
  
    template_name = 'topics/index.html'
    context_object_name = 'latest_topic_list'

    def get_queryset(self):
        """
        返回最新的5条topic(未来的topic将被排除)
        """
        return Topic.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
'''
    latest_topic_list = Topic.objects.order_by('-pub_date')[:5]
    context = { 'latest_topic_list': latest_topic_list }
    return render(request, 'topics/index.html', context)
 '''

class DetailView(generic.DetailView):
    model = Topic
    template_name = 'topics/detail.html'

'''
    topic = get_object_or_404(Topic, pk=topic_id)
    return render(request, 'topics/detail.html', {'topic': topic})
'''
def reply(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    if request.POST['reply_content']:
        new_reply = topic.reply_set.create(content=request.POST['reply_content'])

    return HttpResponseRedirect(reverse('topics:detail', args=(topic.id, )))

def r_vote(request):
    reply_id = request.POST['reply_id']
    if reply_id:
        reply = get_object_or_404(Reply, pk=reply_id)
        reply.votes += 1
        reply.save()

    return HttpResponseRedirect(reverse('topics:detail', args=(reply.topic.id, )))
