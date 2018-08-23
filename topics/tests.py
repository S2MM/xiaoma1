import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Topic

class TopicModelTests(TestCase):
    def test_was_published_recently_with_future_topic(self):
        '''
            未来发布的topic调用was_published_recently()返回False。
        '''
        time = timezone.now() + datetime.timedelta(days=30)
        future_topic = Topic(pub_date=time)
        self.assertIs(future_topic.was_published_recently(), False)

    def test_was_published_recently_with_old_topic(self):
        '''
            一天前发布的topic调用was_published_recently()返回False。
        '''
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        future_topic = Topic(pub_date=time)
        self.assertIs(future_topic.was_published_recently(), False)

    def test_was_published_recently_with_recent_topic(self):
        '''
            24小时内发布的topic调用was_published_recently()返回False。
        '''
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        future_topic = Topic(pub_date=time)
        self.assertIs(future_topic.was_published_recently(), True)

class TopicIndexViewTests(TestCase):
    def test_no_topic(self):
        '''
            当没有Topic时
        '''
        response = self.client.get(reverse('topics:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "没有话题")
        self.assertQuerysetEqual(response.context['latest_topic_list'], [])


def create_topic(title, content, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Topic.objects.create(title=title, content=contnet, pub_date=time)