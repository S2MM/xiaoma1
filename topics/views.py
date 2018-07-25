from django.shortcuts import render
from django.http import HttpResponse

from .models import Topic

def index(request):
    latest_topic_list = Topic.objects.order_by('-pub_date')[:5]
    output = ', '.join([t.title for t in latest_topic_list])
    return HttpResponse(output)

def detail(request, topic_id):
    return HttpResponse("你在看话题%s详情页面" % topic_id)

def reply(request, topic_id):
    return HttpResponse("你回复了话题%s." % topic_id)

    
