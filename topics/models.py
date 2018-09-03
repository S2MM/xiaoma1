import datetime

from django.db import models
from django.utils import timezone

from tinymce import HTMLField

class Topic(models.Model):
    title = models.CharField(max_length=50)
    content = HTMLField('话题内容')
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.title

class Reply(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    pub_date = models.DateTimeField(default=timezone.now())

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.content


