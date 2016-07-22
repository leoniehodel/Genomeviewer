from django.conf.urls import url
from . import views

app_name = 'genomebrowser'

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^(?P<genome_id>[0-9]+)/$', views.detail, name='detail'),

    url(r'^genome_form/$', views.genome_form, name='genome_form'),

    url(r'^(?P<genome_id>[0-9]+)/delete_genome/$', views.delete_genome,
        name='delete_genome'),

]
