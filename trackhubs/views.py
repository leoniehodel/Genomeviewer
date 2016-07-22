from django.shortcuts import render, get_object_or_404
from .forms import TrackHubForm, TrackForm
from .models import TrackHub, Track
import os, shutil
# Create your views here.


def create_trackhub(request):
    form = TrackHubForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        #save the input of the form
        trackhub = form.save(commit=False)
        trackhub.save()
        if not os.path.isdir(os.path.join(trackhub.hub_name)):
            #generate track hub directory
            os.makedirs(os.path.join(trackhub.hub_name))
            hub = open(os.path.join(trackhub.hub_name, 'hub.txt'), 'w')
            hub.write(makehubfile(trackhub))
            hub.close()
            genomes = open(os.path.join(trackhub.hub_name,'genomes.txt'), 'w')
            genomes.write(makegenomesfile(trackhub))
            genomes.close()
        return render(request, 'trackhubs/detail.html', {'trackhub': trackhub})
    return render(request, 'trackhubs/create_trackhub.html', {'form': form})


def index(request):
    trackhubs = TrackHub.objects.all()
    return render(request, 'trackhubs/index.html', {'trackhubs': trackhubs})


def detail(request, trackhub_id):
    trackhub = get_object_or_404(TrackHub, pk=trackhub_id)
    return render(request, 'trackhubs/detail.html', {'trackhub': trackhub})


def create_track(request, trackhub_id):
    form = TrackForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        track = form.save(commit=False)
        track.save()
        trackhub = TrackHub.objects.get(pk=trackhub_id)
        maketrackDbfile(trackhub)
        return render(request, 'trackhubs/detail.html', {'trackhub': trackhub})
    return render(request, 'trackhubs/create_track.html', {'form': form})


def delete_trackhub(request,trackhub_id):
    trackhub = TrackHub.objects.get(pk=trackhub_id)
    #how can I ask for confirmation before deletion??
    trackhub.delete()
    if os.path.isdir(os.path.join(trackhub.hub_name)):
        shutil.rmtree(trackhub.hub_name)
    return render(request, 'trackhubs/index.html', {'trackhub': trackhub})


def delete_track(request,track_id, trackhub_id):
    trackhub = get_object_or_404(TrackHub, pk=trackhub_id)
    track = Track.objects.get(pk=track_id)
    track.delete()
    maketrackDbfile(trackhub)
    return render(request, 'trackhubs/detail.html', {'trackhub': trackhub})


def makehubfile(trackhub):
    return ("hub   "+trackhub.hub_name+"\nshortlabel   "+trackhub.short_label+"\nlonglabel   "+trackhub.long_label +
            "\nemail   "+trackhub.email)


def makegenomesfile(trackhub):
    return ("genome   "+trackhub.Genome.ucscName+"\ntrackDb   "+trackhub.Genome.ucscName+"/trackDb")


def maketrackDbfile(th):
    path = str(th.hub_name) + '/' + str(th.Genome.ucscName)
    if not os.path.isdir(os.path.join(path)):
        os.makedirs(os.path.join(th.hub_name, th.Genome.ucscName))
    trackDb = open(os.path.join(path, 'trackDb.txt'), 'w')
    s = ''
    for track in th.track_set.all():
        s += ("track   "+track.name+"\nshortlabel   "+track.short_label+"\nlonglabel   "+track.long_label+
        '\ntype   '+track.track_type+"\nbigDataUrl   "+track.url+"\n\n")
    trackDb.write(s)
    trackDb.close()

