from django.conf.urls import url
from . import views

app_name = 'trackhubs'

urlpatterns = [

    url(r'^$', views.index, name='index'),

    url(r'^(?P<trackhub_id>[0-9]+)/$', views.detail, name='detail'),

    url(r'^create_trackhub/$', views.create_trackhub, name='create_trackhub'),

    url(r'^(?P<trackhub_id>[0-9]+)/create_track/$', views.create_track, name='create_track'),

    url(r'^(?P<trackhub_id>[0-9]+)/delete_trackhub/$', views.delete_trackhub, name='delete_trackhub'),

    url(r'^(?P<trackhub_id>[0-9]+)/delete_track/(?P<track_id>[0-9]+)/$', views.delete_track, name='delete_track'),

]
