from django.shortcuts import render, get_object_or_404
from .models import Genome
from .forms import GenomeForm
# Create your views here. they are functions, user request something and you give something back.


def genome_form(request):
    form = GenomeForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        genome = form.save(commit=False)
        genome.save()
        return render(request, 'genomebrowser/index.html', {'genome': genome})
    return render(request, 'genomebrowser/genome_form.html', {'form': form})


def delete_genome(request, genome_id):
    genome = Genome.objects.get(id=genome_id)
    genome.delete()
    return render(request, 'genomebrowser/index.html', {'genome': genome})


def detail(request, genome_id):
    genome = get_object_or_404(Genome, pk=genome_id)
    return render(request, 'genomebrowser/detail.html', {'genome': genome})


def index(request):
    genomes = Genome.objects.all()
    return render(request, 'genomebrowser/index.html', {'genomes': genomes})
