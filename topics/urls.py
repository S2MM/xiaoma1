from django.urls import path

from . import views

app_name = 'topics'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:topic_id>/reply', views.reply, name='reply' ),
    path('r_vote/', views.r_vote, name='r_vote'),
]

