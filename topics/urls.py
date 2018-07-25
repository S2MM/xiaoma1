from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:topic_id>/', views.detail, name='detail'),
    path('<int:topic_id>/reply', views.reply, name='reply' )
    
]

